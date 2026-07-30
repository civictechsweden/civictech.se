# civictech.se

Website for [Civic Tech Sweden](https://civictech.se), the Swedish network for civic tech.

If you want to add or edit content, open a pull request, [open an issue](https://github.com/civictechsweden/civictech.se/issues), or ask in [Matrix](https://app.element.io/#/room/#civictechse:matrix.org) / hello(at)civictech.se if you prefer not to edit the repo yourself.

## Development

Requires **Ruby 3.4+**, **Bundler**, and **Node.js 20+** (for [Bulma](https://bulma.io)).

If you use `rbenv` / `asdf` / RVM and want to match CI exactly: **Ruby 3.4.2** (see [`.ruby-version`](.ruby-version)).  
Without a version manager, any system Ruby **3.4+** works after `bundle install`.

```bash
npm install
bundle install
```

Jekyll 4 is installed via Bundler in this project (`gem "jekyll", "~> 4.4"` in `Gemfile`) — you do not need a global Jekyll install.

**Always use `bundle exec`** in front of `jekyll`. If you run the system `jekyll` (e.g. `/usr/bin/jekyll` from Ubuntu) you can get dependency conflicts such as:

```text
You have already activated public_suffix 6.0.2, but your Gemfile requires public_suffix 7.0.5
```

Fix: `bundle exec jekyll build` instead of `jekyll build`.

The site is built with **Jekyll 4** + **Bulma 1**. Production is [civictech.se](https://civictech.se) via **GitHub Pages** (custom domain in `CNAME`), deployed by **GitHub Actions**.

### Verify locally

Run from the project root before you commit and push:

```bash
npm ci
bundle exec jekyll build --trace
```

### Preview in the browser

```bash
bundle exec jekyll serve
```

Open [http://127.0.0.1:4000/](http://127.0.0.1:4000/) (or the port Jekyll prints). Stop with `Ctrl+C`, or:

```bash
pkill -f 'jekyll serve'
```

### Branches and publishing

GitHub Pages is set to **GitHub Actions** (not “Deploy from a branch”). Pushes to **`main`** run [Deploy Jekyll site to Pages](.github/workflows/deploy-pages.yml), which builds with Bundler + npm and deploys the artifact.

| Branch | Role | Deploy on push |
|--------|------|----------------|
| `develop` | Day-to-day work | No |
| `main` | Production → [civictech.se](https://civictech.se) | Yes (GitHub Actions → Pages) |

Flow: feature branch → PR → `develop` → PR → `main` → workflow deploys.

### Publish a change

```bash
git checkout develop
git pull origin develop
git checkout -b your-feature-branch
# ... make changes ...
git add -A
git commit -m "Describe your change"
git push origin your-feature-branch
```

Open a pull request against `develop`. When the change should go live: PR `develop` → `main` (Actions deploys from `main`).

## Content

| Path | What it is |
|------|------------|
| `_blog/` | Blog posts (collection `blog`, URLs under `/blog/`) |
| `_posts/` | Projects (permalink under `/projects/`) |
| `_events/` | Events |
| `_groups/` | Local groups |
| `en/` | English pages |
| `_data/menu.yml` | Top navigation (SV + EN) |
| `_includes/` | Shared layout pieces (menu, footer, social icons, …) |

### Blog import from Medium

Blog posts live in `_blog/` and are separate from **projects** in `_posts/`.

To import or re-import from Medium (URL list in `scripts/medium-blog-urls.txt`):

```bash
# optional: refresh RSS cache
curl -sL -A "Mozilla/5.0" "https://medium.com/feed/civictechsweden" -o tmp/medium-cache/feed.xml
python3 scripts/import_medium_blog.py --rss-file tmp/medium-cache/feed.xml
```

Add any remaining Medium post URLs to `scripts/medium-blog-urls.txt`, then re-run the importer.

## Contribute

- Code and content: pull requests against `develop`.
- Ideas, typos, and link tips: [GitHub Issues](https://github.com/civictechsweden/civictech.se/issues).
- Chat: [Matrix room `#civictechse:matrix.org`](https://app.element.io/#/room/#civictechse:matrix.org).

## License

See [LICENSE](LICENSE) (GNU GPL v3).

## Contact

Matrix: [\#civictechse:matrix.org](https://app.element.io/#/room/#civictechse:matrix.org)  
Email: hello(at)civictech.se
