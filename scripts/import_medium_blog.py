#!/usr/bin/env python3
"""
Import Medium posts listed in scripts/medium-blog-urls.txt into _blog/.

Prefers full HTML from the publication RSS feed when available; otherwise
attempts a best-effort page fetch (may fail under Cloudflare).

Usage (from repo root):
  python3 scripts/import_medium_blog.py
  python3 scripts/import_medium_blog.py --urls scripts/medium-blog-urls.txt
"""

from __future__ import annotations

import argparse
import html
import json
import re
import ssl
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_URLS = ROOT / "scripts" / "medium-blog-urls.txt"
BLOG_DIR = ROOT / "_blog"
UPLOAD_DIR = ROOT / "_uploads" / "blog"
CACHE_DIR = ROOT / "tmp" / "medium-cache"
RSS_URL = "https://medium.com/feed/civictechsweden"
UA = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)

NS = {
    "content": "http://purl.org/rss/1.0/modules/content/",
    "dc": "http://purl.org/dc/elements/1.1/",
    "atom": "http://www.w3.org/2005/Atom",
}

# Known bilingual pairs (medium post ids) → shared ref
KNOWN_REFS = {
    "760a46ed3b3c": "almedalsdata",
    "267eb6865860": "almedalsdata",
}


def http_get(url: str, timeout: int = 45) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    ctx = ssl.create_default_context()
    with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
        return resp.read()


def normalize_url(url: str) -> str:
    url = url.strip()
    if not url or url.startswith("#"):
        return ""
    parts = urllib.parse.urlsplit(url)
    # drop query/fragment
    path = parts.path.rstrip("/")
    return urllib.parse.urlunsplit((parts.scheme or "https", parts.netloc, path, "", ""))


def medium_id_from_url(url: str) -> str | None:
    # …-dc8ca8e9dab7 or /p/dc8ca8e9dab7
    m = re.search(r"-([a-f0-9]{8,16})$", urllib.parse.urlsplit(url).path)
    if m:
        return m.group(1)
    m = re.search(r"/p/([a-f0-9]{8,16})", url)
    if m:
        return m.group(1)
    return None


def slug_from_url(url: str, medium_id: str | None) -> str:
    path = urllib.parse.unquote(urllib.parse.urlsplit(url).path)
    base = path.rstrip("/").split("/")[-1]
    if medium_id and base.endswith("-" + medium_id):
        base = base[: -(len(medium_id) + 1)]
    # fold accents: å→a etc.
    base = unicodedata.normalize("NFKD", base)
    base = "".join(c for c in base if not unicodedata.combining(c))
    base = re.sub(r"[^a-zA-Z0-9]+", "-", base).strip("-").lower()
    return base or (medium_id or "post")


def load_urls(path: Path) -> list[str]:
    urls = []
    for line in path.read_text(encoding="utf-8").splitlines():
        u = normalize_url(line)
        if u:
            urls.append(u)
    # dedupe preserve order
    seen = set()
    out = []
    for u in urls:
        if u not in seen:
            seen.add(u)
            out.append(u)
    return out


def load_rss(rss_path: Path | None = None) -> dict[str, dict]:
    """Map medium_id -> post fields from RSS."""
    by_id: dict[str, dict] = {}
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cached = CACHE_DIR / "feed.xml"
    data = None
    if rss_path and rss_path.is_file():
        data = rss_path.read_bytes()
        print(f"RSS: using file {rss_path}")
    elif cached.is_file() and cached.stat().st_size > 1000:
        data = cached.read_bytes()
        print(f"RSS: using cache {cached}")
    else:
        try:
            data = http_get(RSS_URL)
            cached.write_bytes(data)
        except Exception as e:
            print(f"WARN: could not fetch RSS: {e}", file=sys.stderr)
            return by_id
    root = ET.fromstring(data)
    for item in root.findall("./channel/item"):
        link = normalize_url(item.findtext("link") or "")
        mid = medium_id_from_url(link) or ""
        guid = item.findtext("guid") or ""
        if not mid and "/p/" in guid:
            mid = guid.rstrip("/").split("/")[-1]
        title = (item.findtext("title") or "").strip()
        author = (item.findtext("dc:creator", default="", namespaces=NS) or "").strip()
        pub = item.findtext("pubDate") or ""
        body = item.findtext("content:encoded", default="", namespaces=NS) or ""
        cats = [c.text for c in item.findall("category") if c.text]
        try:
            dt = parsedate_to_datetime(pub)
        except Exception:
            dt = datetime.now(timezone.utc)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        entry = {
            "title": title,
            "author": author,
            "date": dt,
            "tags": cats,
            "body_html": body,
            "medium_url": link,
            "medium_id": mid,
        }
        if mid:
            by_id[mid] = entry
        by_id[link] = entry
    print(f"RSS: loaded {len([k for k in by_id if len(k) <= 16])} post id(s)")
    return by_id


def strip_medium_footer(html_body: str) -> str:
    # Remove tracking pixel and "originally published" footer
    html_body = re.sub(
        r'<img[^>]+medium\.com/_/stat[^>]*>',
        "",
        html_body,
        flags=re.I,
    )
    html_body = re.sub(
        r"<hr\s*/?>\s*<p>\s*<a[^>]*>.*?</a>\s*was originally published.*?</p>\s*$",
        "",
        html_body,
        flags=re.I | re.S,
    )
    return html_body.strip()


def first_image_src(html_body: str) -> str | None:
    m = re.search(r'<img[^>]+src=["\']([^"\']+)["\']', html_body, flags=re.I)
    return m.group(1) if m else None


def download_image(url: str, dest_dir: Path, index: int, retries: int = 4) -> str | None:
    """Download image; return site-relative path or None."""
    raw = None
    last_err = None
    for attempt in range(retries):
        try:
            raw = http_get(url)
            break
        except Exception as e:
            last_err = e
            wait = 2 ** attempt
            print(f"  WARN: image attempt {attempt+1} failed ({e}); sleep {wait}s")
            time.sleep(wait)
    if raw is None:
        print(f"  WARN: image failed {url}: {last_err}")
        return None
    # guess extension
    path = urllib.parse.urlsplit(url).path
    ext = Path(path).suffix.lower()
    if ext not in {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"}:
        if raw[:3] == b"\xff\xd8\xff":
            ext = ".jpg"
        elif raw[:8] == b"\x89PNG\r\n\x1a\n":
            ext = ".png"
        elif raw[:4] == b"GIF8":
            ext = ".gif"
        else:
            ext = ".jpg"
    name = f"{index:02d}{ext}"
    dest_dir.mkdir(parents=True, exist_ok=True)
    (dest_dir / name).write_bytes(raw)
    rel = f"/uploads/blog/{dest_dir.name}/{name}"
    return rel


def rewrite_images(html_body: str, slug: str) -> tuple[str, str | None]:
    dest = UPLOAD_DIR / slug
    hero = None
    idx = 0
    out = html_body
    # unique remote srcs in order of appearance
    seen: set[str] = set()
    ordered: list[str] = []
    for m in re.finditer(r'src=["\'](https?://[^"\']+)["\']', html_body):
        src = m.group(1)
        if src in seen:
            continue
        seen.add(src)
        ordered.append(src)
    for src in ordered:
        if "medium.com/_/stat" in src:
            out = out.replace(src, "")
            continue
        idx += 1
        local = download_image(src, dest, idx)
        if local:
            if hero is None:
                hero = local
            out = out.replace(src, local)
    out = re.sub(r'<img[^>]+src=["\']["\'][^>]*>', "", out)
    return out, hero

def html_to_markdownish(html_body: str) -> str:
    """Lightweight HTML→Markdown (stdlib only). Keeps tables/pre as HTML if complex."""
    text = html_body
    # figures → image + caption
    def fig_repl(m: re.Match) -> str:
        block = m.group(0)
        img = re.search(r'src=["\']([^"\']+)["\']', block)
        cap = re.search(r"<figcaption[^>]*>(.*?)</figcaption>", block, flags=re.I | re.S)
        parts = []
        if img:
            parts.append(f"\n\n![]({img.group(1)})\n")
        if cap:
            cap_txt = re.sub(r"<[^>]+>", "", cap.group(1))
            cap_txt = html.unescape(cap_txt).strip()
            if cap_txt:
                parts.append(f"*{cap_txt}*\n")
        return "".join(parts) or block

    text = re.sub(r"<figure\b[^>]*>.*?</figure>", fig_repl, text, flags=re.I | re.S)
    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.I)
    text = re.sub(r"<hr\s*/?>", "\n\n---\n\n", text, flags=re.I)

    def heading(m: re.Match) -> str:
        level = int(m.group(1))
        inner = re.sub(r"<[^>]+>", "", m.group(2))
        inner = html.unescape(inner).strip()
        return f"\n\n{'#' * level} {inner}\n\n"

    text = re.sub(r"<h([1-6])[^>]*>(.*?)</h\1>", heading, text, flags=re.I | re.S)

    def link(m: re.Match) -> str:
        href = m.group(1)
        inner = re.sub(r"<[^>]+>", "", m.group(2))
        inner = html.unescape(inner).strip()
        return f"[{inner}]({href})"

    text = re.sub(r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', link, text, flags=re.I | re.S)

    def img(m: re.Match) -> str:
        src = m.group(1)
        alt = m.group(2) or ""
        return f"\n\n![{html.unescape(alt)}]({src})\n\n"

    text = re.sub(
        r'<img[^>]+src=["\']([^"\']+)["\'][^>]*(?:alt=["\']([^"\']*)["\'])?[^>]*/?>',
        img,
        text,
        flags=re.I,
    )
    # second pass for alt before src
    text = re.sub(
        r'<img[^>]+alt=["\']([^"\']*)["\'][^>]+src=["\']([^"\']+)["\'][^>]*/?>',
        lambda m: f"\n\n![{html.unescape(m.group(1))}]({m.group(2)})\n\n",
        text,
        flags=re.I,
    )

    def li(m: re.Match) -> str:
        inner = re.sub(r"<[^>]+>", "", m.group(1))
        return f"- {html.unescape(inner).strip()}\n"

    text = re.sub(r"<li[^>]*>(.*?)</li>", li, text, flags=re.I | re.S)
    text = re.sub(r"</?ul[^>]*>", "\n", text, flags=re.I)
    text = re.sub(r"</?ol[^>]*>", "\n", text, flags=re.I)

    def pre(m: re.Match) -> str:
        inner = m.group(1)
        inner = re.sub(r"<br\s*/?>", "\n", inner, flags=re.I)
        inner = re.sub(r"<[^>]+>", "", inner)
        inner = html.unescape(inner)
        return f"\n\n```\n{inner.strip()}\n```\n\n"

    text = re.sub(r"<pre[^>]*>(.*?)</pre>", pre, text, flags=re.I | re.S)
    text = re.sub(r"<blockquote[^>]*>(.*?)</blockquote>", lambda m: "\n\n> " + re.sub(r"<[^>]+>", "", html.unescape(m.group(1))).strip().replace("\n", "\n> ") + "\n\n", text, flags=re.I | re.S)

    text = re.sub(r"<(strong|b)[^>]*>(.*?)</\1>", r"**\2**", text, flags=re.I | re.S)
    text = re.sub(r"<(em|i)[^>]*>(.*?)</\1>", r"*\2*", text, flags=re.I | re.S)
    text = re.sub(r"<p[^>]*>(.*?)</p>", lambda m: "\n\n" + re.sub(r"<[^>]+>", "", html.unescape(m.group(1))).strip() + "\n\n", text, flags=re.I | re.S)
    text = re.sub(r"<div[^>]*>", "\n", text, flags=re.I)
    text = re.sub(r"</div>", "\n", text, flags=re.I)
    text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def detect_lang(title: str, tags: list[str], body: str) -> str:
    tags_l = {t.lower() for t in tags}
    if "english" in tags_l:
        return "en"
    # Heuristic: high ratio of English stopwords / few Swedish chars
    sample = (title + " " + body[:2000]).lower()
    if re.search(r"[åäö]", sample):
        return "sv"
    en_markers = len(re.findall(r"\b(the|and|with|that|this|from|for|are|was|were|have)\b", sample))
    sv_markers = len(re.findall(r"\b(och|att|det|som|för|är|på|en|ett|vi|om)\b", sample))
    if en_markers > sv_markers + 3:
        return "en"
    return "sv"


def yaml_quote(s: str) -> str:
    s = s.replace('"', '\\"')
    return f'"{s}"'


def excerpt_from_body(md: str, limit: int = 200) -> str:
    # first non-empty non-heading non-image paragraph
    skip_re = re.compile(
        r"^(swedish|english|svensk|engelsk)\s+version",
        re.I,
    )
    for para in re.split(r"\n\s*\n", md):
        p = para.strip()
        if not p or p.startswith("#") or p.startswith("!["):
            continue
        p = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", p)
        p = re.sub(r"[*_`]", "", p)
        p = re.sub(r"\s+", " ", p).strip()
        if skip_re.match(p) or p.upper() in {"SWEDISH VERSION HERE", "ENGLISH VERSION HERE"}:
            continue
        if len(p) > limit:
            return p[: limit - 1].rstrip() + "…"
        return p
    return ""


def write_post(entry: dict, slug: str) -> Path:
    mid = entry["medium_id"]
    lang = entry["lang"]
    ref = KNOWN_REFS.get(mid or "", "")
    date: datetime = entry["date"]
    date_str = date.strftime("%Y-%m-%d %H:%M:%S %z")
    if date_str.endswith("0000"):
        # normalize +0000 → +00:00 for readability
        date_str = date.astimezone(timezone.utc).strftime("%Y-%m-%d %H:%M:%S +00:00")

    tags = entry.get("tags") or []
    tags_yaml = "[" + ", ".join(yaml_quote(t) for t in tags) + "]" if tags else "[]"
    body = entry["body_md"]
    excerpt = excerpt_from_body(body)
    image = entry.get("image") or ""

    # file name: include lang suffix for non-default en twin
    fname = f"{date.strftime('%Y-%m-%d')}-{slug}"
    if lang == "en":
        fname += "-en"
    path = BLOG_DIR / f"{fname}.md"

    fm = [
        "---",
        f"title: {yaml_quote(entry['title'])}",
        f"date: {date.strftime('%Y-%m-%d %H:%M:%S %z') if date.tzinfo else date.strftime('%Y-%m-%d %H:%M:%S') + ' +00:00'}",
        f"lang: {lang}",
        f"ref: {ref}" if ref else "ref:",
        f"author: {yaml_quote(entry.get('author') or 'Civic Tech Sweden')}",
        f"tags: {tags_yaml}",
        f"excerpt: {yaml_quote(excerpt)}",
        f"image: {image}" if image else "image:",
        f"medium_url: {entry['medium_url']}",
        f"medium_id: {mid or ''}",
        "---",
        "",
        body,
    ]
    # Fix date format to always have colon in offset if possible
    # Python %z gives +0000; Jekyll accepts it. Leave as iso-like:
    dt = entry["date"]
    if dt.tzinfo:
        off = dt.strftime("%z")
        if len(off) == 5:
            off = off[:3] + ":" + off[3:]
        date_line = f"date: {dt.strftime('%Y-%m-%d %H:%M:%S')} {off}"
    else:
        date_line = f"date: {dt.strftime('%Y-%m-%d %H:%M:%S')} +00:00"
    fm[2] = date_line

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(fm), encoding="utf-8")
    return path


def try_fetch_page(url: str) -> dict | None:
    """Best-effort fetch; Medium often returns Cloudflare HTML."""
    try:
        raw = http_get(url)
    except Exception as e:
        print(f"  fetch failed: {e}")
        return None
    text = raw.decode("utf-8", errors="replace")
    if "Just a moment" in text or "cf-browser-verification" in text or "challenge-platform" in text:
        print("  blocked by Cloudflare")
        return None
    # Try ld+json
    for m in re.finditer(
        r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
        text,
        flags=re.I | re.S,
    ):
        try:
            data = json.loads(m.group(1))
        except json.JSONDecodeError:
            continue
        objs = data if isinstance(data, list) else [data]
        for obj in objs:
            if not isinstance(obj, dict):
                continue
            if obj.get("@type") in ("Article", "BlogPosting", "NewsArticle") or "headline" in obj:
                body = obj.get("articleBody") or ""
                title = obj.get("headline") or obj.get("name") or ""
                author = ""
                a = obj.get("author")
                if isinstance(a, dict):
                    author = a.get("name") or ""
                elif isinstance(a, list) and a:
                    author = (a[0] or {}).get("name") or ""
                date_s = obj.get("datePublished") or ""
                try:
                    dt = datetime.fromisoformat(date_s.replace("Z", "+00:00"))
                except Exception:
                    dt = datetime.now(timezone.utc)
                if body:
                    return {
                        "title": title,
                        "author": author,
                        "date": dt,
                        "tags": [],
                        "body_html": f"<p>{html.escape(body)}</p>" if "<" not in body else body,
                        "medium_url": normalize_url(url),
                        "medium_id": medium_id_from_url(url) or "",
                    }
    # meta og:title fallback insufficient without body
    print("  no usable article body in HTML")
    return None


def import_one(url: str, rss_index: dict) -> bool:
    mid = medium_id_from_url(url)
    entry = None
    if mid and mid in rss_index:
        entry = dict(rss_index[mid])
        print(f"OK RSS id={mid}: {entry['title'][:60]}")
    elif url in rss_index:
        entry = dict(rss_index[url])
        print(f"OK RSS url: {entry['title'][:60]}")
    else:
        print(f"FETCH {url}")
        entry = try_fetch_page(url)
        if not entry:
            return False

    entry["medium_url"] = normalize_url(entry.get("medium_url") or url)
    entry["medium_id"] = entry.get("medium_id") or mid or medium_id_from_url(entry["medium_url"]) or ""
    slug = slug_from_url(entry["medium_url"], entry["medium_id"])
    body = strip_medium_footer(entry["body_html"])
    body, hero = rewrite_images(body, slug)
    entry["image"] = hero or ""
    entry["body_md"] = html_to_markdownish(body)
    entry["lang"] = detect_lang(entry["title"], entry.get("tags") or [], entry["body_md"])
    path = write_post(entry, slug)
    print(f"  → {path.relative_to(ROOT)} ({entry['lang']})")
    return True


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--urls", type=Path, default=DEFAULT_URLS)
    ap.add_argument("--rss-file", type=Path, default=None, help="Use local RSS XML instead of network")
    args = ap.parse_args()
    if not args.urls.is_file():
        print(f"URL list not found: {args.urls}", file=sys.stderr)
        return 1

    urls = load_urls(args.urls)
    print(f"URLs to import: {len(urls)}")
    rss_index = load_rss(args.rss_file)

    ok = 0
    fail = []
    for url in urls:
        try:
            if import_one(url, rss_index):
                ok += 1
            else:
                fail.append(url)
        except Exception as e:
            print(f"  ERROR: {e}")
            fail.append(url)

    print(f"\nDone: {ok} imported, {len(fail)} failed")
    if fail:
        print("Failed URLs:")
        for u in fail:
            print(f"  {u}")
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
