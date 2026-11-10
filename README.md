# xtyao66.github.io

Source for Xiteng Yao's academic website, <https://xtyao66.github.io>.
Built with the [al-folio](https://github.com/alshedivat/al-folio) Jekyll starter (v1.x),
which replaced the earlier Academic Pages template in November 2026. The old version
is still in this repository's Git history.

## Layout

| Path | What it holds |
| --- | --- |
| `_pages/about.md` | Home page: bio, research interests, news, selected papers |
| `_bibliography/papers.bib` | All publications; the publications page, "selected papers" and each research page's paper list are generated from it |
| `_projects/` | One page per research thread, shown at `/research/` (`category: current` or `earlier`, ordered by `importance`) |
| `_pages/experience.md` | Internships and research as a timeline, then teaching and service, at `/experience/` |
| `tools/make_diagrams.py` | Draws the schematic system diagrams; writes `_includes/diagrams/*.svg` (inline, follows light/dark mode) and `assets/img/publication_preview/*.svg` (paper thumbnails and research cards). Edit the script, then run `python tools/make_diagrams.py`; don't hand-edit the SVGs |
| `assets/css/main.scss`, `_sass/_site.scss` | Local copy of the theme's stylesheet entry with a blue accent color, plus this site's own styles (diagram colors, number tiles, experience timeline). After an al-folio upgrade, diff `main.scss` against the gem's copy |
| `assets/pdf/cv.pdf` | The CV, embedded at `/cv/` and linked from the home-page icons. To update it, replace this file and keep the name |
| `_layouts/bib.liquid` | Local copy of the theme's publication-entry template: wider thumbnails, the `award` field shown as a trophy line linking to `/awards/`, the DOI button labelled by publisher (IEEE Xplore / ACM DL), "Abstract" and "Cite" labels, and `html` values starting with `/` treated as site paths ("Paper page") |
| `_includes/news.liquid` | Local copy of the theme's news list: a news item with `date_precision: month` shows month and year only |
| `_news/` | Dated announcements on the home page |
| `_data/socials.yml` | Email, Google Scholar, GitHub, LinkedIn |
| `_data/coauthors.yml`, `_data/venues.yml` | Co-author links and venue badge colors for the publication list |
| `_config.yml` | Site settings |

Layouts, styles and features come from the `al_folio_*` gems (see `Gemfile`), not from
this repository, except for the three local overrides above (`main.scss`, `bib.liquid`,
`news.liquid`). After an al-folio upgrade, diff each against the gem's copy.

Keep page `description` fields plain text: the theme also writes them into `<meta>` tags,
so HTML or quotes there leak onto the page.

## Google Scholar

Papers are indexed from their publisher pages (DOIs) and from the PDFs HPEC hosts. If a
paper ever needs a self-hosted copy for Scholar before its publisher version appears, add a
static `publications/<paper>/index.html` with the `citation_*` tags from
[Google Scholar's inclusion guidelines](https://scholar.google.com/intl/en/scholar/inclusion.html)
and put the PDF in the same folder (`citation_pdf_url` must point at or below the page's own
directory). For IEEE papers, post only the accepted manuscript with IEEE's copyright notice.

## Preview locally

Requires Docker. From this folder:

```bash
docker compose up
```

Then open <http://localhost:8080>. Stop with Ctrl+C, then `docker compose down`.

## Deploy

Pushing to `main` runs `.github/workflows/deploy.yml`, which builds the site and pushes
the result to the `gh-pages` branch. In the repository's Settings → Pages, the source
must be "Deploy from a branch", branch `gh-pages`, folder `/ (root)`.

## License

Template code is MIT-licensed by the al-folio authors (see `LICENSE`). Site content
(text and papers) belongs to its authors; papers carry their publishers' notices.
