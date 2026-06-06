# CLAUDE.md

Guidance for AI assistants working in this repository.

## What this is

The **scientific hub of Carlo Cosentino** — a personal academic website published at
<https://carlocosentino.github.io/>. Carlo is a labour-law professor (Professor Adjunto,
Faculdade de Direito do Recife / UFPE) and lawyer; the site aggregates his publications,
research lines, news, talks, and links to academic profiles.

It is a **static site built with [Hugo](https://gohugo.io/) + [HugoBlox](https://hugoblox.com/)**
(the "Academic CV" template). The site is **monolingual Portuguese (pt-BR)**.

> This is a **content-first repository**. The overwhelming majority of changes are edits to
> Markdown content and YAML config — *not* application code. The theme/engine itself lives in
> external Hugo Modules (Go), **not** in this repo. Do not expect to find or modify theme
> internals here unless you are deliberately overriding a layout (see "Custom overrides").

## Tech stack & key versions

| Thing | Value | Source of truth |
| --- | --- | --- |
| Static site generator | Hugo **Extended** | `hugoblox.yaml` → `build.hugo_version` (currently `0.162.1`) |
| Theme | HugoBlox Academic CV (Hugo Modules) | `go.mod`, `config/_default/module.yaml` |
| CSS | Tailwind CSS v4 (`@tailwindcss/cli`) | `package.json` |
| Module system | Go modules | `go.mod` / `go.sum` (Go 1.19+) |
| Node (CI) | 22 | `.github/workflows/build.yml` |
| Hosting | GitHub Pages | `hugoblox.yaml` → `deploy.host` |

## Repository layout

```
.
├── config/_default/        # All site configuration (YAML)
│   ├── hugo.yaml           # Hugo core: baseURL, language, outputs, markup, taxonomies
│   ├── params.yaml         # HugoBlox config: identity, theme, header/footer, SEO, etc.
│   ├── menus.yaml          # Top navigation menu
│   ├── languages.yaml      # Languages (pt only; en is disabled)
│   └── module.yaml         # Hugo Module imports + mounts
├── content/                # All page content (Markdown). THE MAIN EDITING SURFACE.
│   ├── _index.md           # Home page (landing, hero + collection blocks)
│   ├── perfil/             # "Perfil" (about) page — landing with custom HTML hero
│   ├── publication/        # Publications, one folder per item (page bundles)
│   ├── post/               # "Notícias" (news/blog posts)
│   ├── projects/           # Research lines / "Projetos de Pesquisa"
│   ├── videos/, podcast/,  # Section landing pages (mostly link out)
│   │   materiais/, slides/, courses/, events/, blog/
│   └── authors/me/         # Author profile for "me" (used by author taxonomy)
├── data/authors/me.yaml    # Structured author data (schema: hugoblox/author/v1)
├── assets/                 # Theme-processed assets (avatars, icons, sharing image)
│   └── media/authors/me.png
├── static/                 # Files served as-is (copied verbatim to site root)
│   ├── img/                # Hero/profile cutout images referenced by custom HTML
│   └── uploads/resume.pdf
├── layouts/_partials/      # LOCAL theme overrides (see "Custom overrides")
├── bib_to_hugo.py          # Local BibTeX → publication pages converter (see "Publications")
├── hugoblox.yaml           # Build (Hugo version) + deploy target config
├── package.json            # Tailwind dev dependencies
└── .github/workflows/      # CI/CD (see "Workflows")
```

## How content works

Pages are Markdown with YAML front matter. There are two main shapes:

1. **Landing pages** (`type: landing`) — e.g. `content/_index.md`, `content/perfil/index.md`,
   and the section `_index.md` files. These are composed of `sections:`, each a HugoBlox
   **block** (`block: markdown`, `block: collection`, etc.) with `content:` and `design:` keys.
   This site leans heavily on `block: markdown` with **inline `<style>` + raw HTML** for the
   custom hero and profile layouts. Raw HTML is allowed because `markup.goldmark.renderer.unsafe: true`
   is set in `hugo.yaml`.

2. **Regular content pages** — e.g. each publication, news post, or project. These are
   [page bundles](https://gohugo.io/content-management/page-bundles/): a folder containing
   `index.md` plus any local assets (`artigo.pdf`, `featured.jpg`).

### Publications (`content/publication/<year-slug>/index.md`)

Front matter conventions used here:
- `authors:` is a list; `"me"` maps to the site owner (resolved via `content/authors/me/` and
  `data/authors/me.yaml`). Co-authors are written as plain display names.
- `publication_types:` uses values like `article-journal`, `chapter`, `book`, `paper-conference`.
- `featured: true` surfaces an item in the home page "Publicações" grid (which filters on
  `featured_only: true` and sorts by `Weight`). Use `weight:` to order featured items.
- `publication:` is the structured venue block (`name`, `volume`, `pages`, `publisher`).
- `links:` with `url: artigo.pdf` attaches a bundled PDF (opened in a new tab via custom JS).

### Authors

There are **two** author representations — keep them in sync when editing the profile:
- `data/authors/me.yaml` — schema `hugoblox/author/v1` (newer structured format).
- `content/authors/me/_index.md` — front matter author profile (`superuser: true`).

## Custom overrides

`layouts/_partials/` contains the **only** site-specific theme code. Everything else comes from
the HugoBlox modules. Be careful here — these override theme behaviour:

- `hooks/head-end/custom-bg.html` — large block of injected CSS/JS that heavily restyles the
  dark theme: site background gradient, card appearance, publication cover handling, full
  (un-clamped) publication summaries, hiding the author card, opening PDFs in new tabs, and a
  script that links a specific co-author's name to their Instagram. **If cards, covers, or the
  dark background look "wrong", this file is almost certainly the cause.**
- `hooks/head-end/github-button.html` — loads the GitHub buttons script.
- `views/card.html` — overrides the collection card view (used by `block: collection`).

When changing visual behaviour, prefer adjusting these hooks/overrides over fighting the theme.
The home/profile pages also carry their own scoped inline CSS inside the Markdown blocks.

## Local development

Requires **Hugo Extended** (matching `hugoblox.yaml`) and **Node.js**. Hugo fetches theme
modules from the network on first run.

```bash
npm install            # install Tailwind tooling (devDependencies)
hugo server            # local dev server with live reload → http://localhost:1313
hugo --minify          # production build into ./public (gitignored)
```

Generated output (`public/`, `resources/`, `node_modules/`, `pagefind/`) is gitignored — never
commit build artifacts.

## CI/CD (`.github/workflows/`)

- **`deploy.yml`** — on push to `main` (or manual): reads deploy host from `hugoblox.yaml`,
  calls `build.yml`, then deploys to GitHub Pages. **Merging to `main` publishes the site.**
- **`build.yml`** — reusable + PR validation: installs deps, sets up Hugo (version from
  `hugoblox.yaml`), builds with `--minify`, uploads the Pages artifact. Runs on every PR to `main`.
- **`upgrade.yml`** — weekly (Mon 05:00) / manual: runs the HugoBlox upgrade CLI and opens a PR
  bumping the theme modules.
- **`import-publications.yml`** — on push to `main` touching `publications.bib`: runs the
  `academic` CLI to convert BibTeX → `content/publications/` and opens a PR.
- **`internal-readme-news.yml`** — HugoBlox-org-only; irrelevant here (guarded by org check).

Most workflows are guarded with `if: github.repository_owner != 'HugoBlox'`.

## Publications: two import paths (mind the mismatch)

There are **two different** BibTeX importers, and they disagree on paths. Be deliberate:

1. **`bib_to_hugo.py`** (local script in this repo): reads `../lattes-cosentino.bib` (one level
   **above** the repo) and writes to **`content/publication/`** (singular) — which matches the
   actual content directory the site uses.
2. **`import-publications.yml`** (CI, official `academic` CLI): triggers on `publications.bib`
   at the repo root and writes to **`content/publications/`** (plural) — which is **not** the
   directory the site renders from.

The live publications live in **`content/publication/`** (singular). When adding or regenerating
publications, target that directory. If you touch the import tooling, reconcile these paths
rather than assuming either is correct.

## Conventions & gotchas

- **Language:** All user-facing content, comments in config, and commit-worthy text are in
  **Portuguese (pt-BR)**. Match that when editing content.
- **Site identity** (name, tagline, theme colours, dark mode) lives in `config/_default/params.yaml`
  under `hugoblox:`. The dark palette (`#0a0a0b` background, `#9db4cc` accent) is intentional and
  echoed in the custom hero/background CSS — keep them consistent if you change one.
- **baseURL** is `https://carlocosentino.github.io/` (`hugo.yaml`). CI overrides it at build time
  for Pages.
- **Navigation** is manual in `menus.yaml` — adding a section folder does not add a menu entry.
- Section `_index.md` "view all / see more" pages mostly link **out** to YouTube, podcast, etc.,
  rather than listing local content.
- Don't edit `go.sum` by hand; let the upgrade workflow or `hugo mod` manage module versions.

## When asked to make changes

- **Add/edit a publication, post, or project** → create/edit a page bundle under the matching
  `content/<section>/` folder, following the front-matter patterns above. Set `featured`/`weight`
  if it should appear on the home page.
- **Change site appearance/colours/nav** → `config/_default/params.yaml`, `menus.yaml`, or the
  `layouts/_partials/hooks/` overrides — not theme internals.
- **Update the bio/profile** → keep `data/authors/me.yaml`, `content/authors/me/_index.md`, and the
  inline text in `content/perfil/index.md` consistent.
- **Verify before pushing** → run `hugo --minify` locally; a clean build is the basic gate the PR
  workflow enforces.
```
