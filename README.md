# Website for Civic Tech Sweden

This is the website for [Civic Tech Sweden](https://civictech.se), the Swedish network for civic tech. If you want to add or edit content, reach out to get editing rights on GitHub — or ask us to help if you prefer not to edit the repo yourself.

## Local development

Requirements: **Ruby 3.4+**, Bundler, and **Node.js** (for Bulma).

```bash
npm install
bundle install
bundle exec jekyll serve
```

Open [http://127.0.0.1:4000](http://127.0.0.1:4000) (or the port Jekyll prints). Stack: **Jekyll 4** + **Bulma 1**.

## Blog

Blog posts live in `_blog/` (collection `blog`, URLs under `/blog/`). They are separate from **projects** in `_posts/`.

To import or re-import from Medium (URL list in `scripts/medium-blog-urls.txt`):

```bash
# optional: refresh RSS cache
curl -sL -A "Mozilla/5.0" "https://medium.com/feed/civictechsweden" -o tmp/medium-cache/feed.xml
python3 scripts/import_medium_blog.py --rss-file tmp/medium-cache/feed.xml
```

Add any remaining Medium post URLs to `scripts/medium-blog-urls.txt`, then re-run the importer.

## Publishing

Pushes to `master` run [GitHub Actions](.github/workflows/deploy-pages.yml), which builds the site and deploys it to **GitHub Pages** on the custom domain **civictech.se**.

## Contact

The best way to contact someone who can help is the [Matrix chat](https://app.element.io/#/room/#civictechse:matrix.org) or hello(at)civictech.se.
