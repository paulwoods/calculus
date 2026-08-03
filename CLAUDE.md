# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A self-study **Calculus 1 course** delivered as static HTML. There is no build system, no
package manager, no tests, and no server-side code. Each file is a hand-authored, fully
self-contained HTML document with inline `<style>` and (for modules) an inline KaTeX bootstrap
`<script>`.

## Viewing / "running"

The pages live in `src/`. Open any file directly in a browser — no build or server step:

```
xdg-open src/calc1_00_index.html
```

A network connection is required at view time: fonts and the KaTeX math renderer load from CDNs
(Google Fonts + `cdnjs.cloudflare.com/.../KaTeX/0.16.9`). For a local server, run
`python3 -m http.server -d src`, or use Docker
(`docker compose -f deploy/docker-compose.yaml up -d`, then http://localhost:8080/) — the
Dockerfile serves `src/` via nginx with `calc1_00_index.html` as the `/` default.

## File layout

All course pages live in `src/`; the repo root holds tooling (`Dockerfile`, `docker-compose.yaml`,
`CLAUDE.md`).

- `src/calc1_00_index.html` — the landing/navigation hub. Links out to all ten modules and is the
  only page that wires cross-file navigation.
- `src/calc1_01_*.html` … `src/calc1_10_*.html` — the ten course modules, numbered in intended
  study order. The numeric prefix is the module's position; ordering is pedagogically load-bearing
  (see the index's "How to use this course" section — each module's tools feed the next).

## Module anatomy

Every module file follows the same top-to-bottom skeleton; match it when editing or adding one:

1. `:root` CSS custom-property block — the design tokens. **This block is copy-pasted into every
   file** (there is no shared stylesheet). Keep it in sync across files when changing the palette.
2. `<link rel="icon">` favicon immediately after `</title>` — an inline `data:image/svg+xml` URI
   (integral sign, `--poly`→`--trig`→`--exp` gradient on `--bg`), byte-identical in every file
   including the index. Then KaTeX `<link>`/`<script defer>` includes + Google Fonts preconnect.
3. `.rail` sticky header → `.hero` (eyebrow with module number, gradient `h1`, `.lede`, and
   usually an inline hand-coded `<svg class="plot">` illustration).
4. **Tutorial** section (`.section-tag` "Tutorial · ~1000 words") — numbered `h2` sub-sections,
   each carrying an `--accent` color.
5. **Practice** section — 20 `.q` cards, each with a `<details><summary>Solution</summary>` that
   hides the worked answer until tapped.
6. A `.next` "next module" card at the bottom.

## Conventions that matter

- **Math is KaTeX/LaTeX** written inline in the HTML as `$...$` (inline) and `$$...$$` (display).
  Rendering happens client-side via the auto-render bootstrap at the end of each module (`throwOnError:false`).
  The index page has no math and no KaTeX include.
- **Color families** are the organizing visual system, defined as tokens and reused everywhere:
  `--poly` (cyan), `--rat` (purple), `--exp` (amber), `--log` (rose), `--trig` (green). Each
  module picks an accent for its `.rail .dot` and `h1` gradient; practice-problem cards cycle
  through the five families via the `--qc` variable; tutorial `h2`s set `--accent`.
- **No shared assets.** Styles, tokens, the favicon data URI, and the KaTeX bootstrap are
  duplicated per file by design. A change to "the CSS" means editing each file, not one central
  place.

## Navigation

Each module's bottom `.next` card links to the following module (`01 → 02 → … → 10`), and module
10's card links back to `calc1_00_index.html`. The `.name` inside each card is the human-readable
label for its target; keep it in sync with the `href` when reordering or renaming modules.
