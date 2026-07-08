# Graph Night — Design System

*"A graphing calculator at night."*

A dark-mode design system for educational and technical content, extracted from a 10-module Calculus 1 course. Built for pages that mix prose, math, diagrams, and interactive reveal-able content.

---

## Philosophy

Three ideas drive every decision:

1. **Color does work, not decoration.** The five accent hues form a semantic cycle — in the original course each mapped to a function family (polynomial = cyan, rational = violet, exponential = amber, logarithm = rose, trig = emerald). In your project, assign each hue a *meaning* (a category, a status, a module) and use it consistently across badges, borders, and section accents. Random color assignment breaks the system.

2. **Monospace = metadata, Grotesk = identity, Plex Sans = reading.** The three typefaces have strict roles. If text describes *the page* (labels, breadcrumbs, counts, annotations), it's IBM Plex Mono, uppercase, letter-spaced. If it *names* something (titles, badges), it's Space Grotesk. Everything you actually read is IBM Plex Sans.

3. **The grid is the room.** The graph-paper background and the framed `figure.plot` establish a "plotting environment" feel. Content sits *on* the grid; figures are windows *into* it.

---

## Files

| File | Purpose |
|---|---|
| `css/graph-night.css` | The full stylesheet. Drop-in, no build step. |
| `starter/starter.html` | Boilerplate page with every component demonstrated. |
| `generator/template_gen.py` | Python generator for stamping out many pages from content dicts (the workflow used to build the course). |

---

## Tokens

### Surfaces

| Token | Value | Use |
|---|---|---|
| `--bg` | `#0a0e17` | Page background (under the grid) |
| `--bg-grid` | `rgba(120,140,180,0.055)` | 32px graph-paper lines |
| `--surface` | `#111725` | Cards, panels |
| `--surface-2` | `#161d2e` | Elevated/hover surfaces |
| `--border` | `rgba(150,170,210,0.12)` | Default hairlines |
| `--border-strong` | `rgba(150,170,210,0.22)` | Hover borders, emphasis rules |

### Ink (text)

| Token | Value | Use |
|---|---|---|
| `--ink` | `#e8eef7` | Body text |
| `--ink-soft` | `#aab4c5` | Secondary text, solutions, descriptions |
| `--ink-faint` | `#6f7b90` | Labels, metadata, annotations |

Bold text (`strong`) renders pure white `#fff` — one step *above* `--ink` — so emphasis reads as brightness, not just weight.

### Accents ("plot colors")

| Token | Hex | Original semantic |
|---|---|---|
| `--poly` | `#38bdf8` | cyan — accent-1 |
| `--rat` | `#c084fc` | violet — accent-2 |
| `--exp` | `#fbbf24` | amber — accent-3 (also the "system" color: eyebrows, focus rings) |
| `--log` | `#fb7185` | rose — accent-4 |
| `--trig` | `#34d399` | emerald — accent-5 |

Accent glow: interactive/badge elements pair their accent with `box-shadow: 0 0 14px -2px <accent>` — the "phosphor glow" that sells the calculator-screen feel. SVG curves get `filter: drop-shadow(0 0 6px currentColor)`.

### Per-page theme knobs

Override these to re-skin a page without touching components:

```css
:root{
  --glow:       rgba(192,132,252,0.12); /* hero radial tint */
  --dot-color:  var(--rat);             /* rail status dot */
  --g1: var(--rat);  --g2: var(--log);  --g3: var(--exp); /* h1 gradient */
  --next-color: var(--exp);             /* footer nav accent */
}
```

In the course, each module rotated these to give every page its own identity inside one system.

### Layout

- `--maxw: 780px` content column (880px works for index/grid pages)
- `--radius: 14px` panels, `10px` small cards, `8px` badges
- Page gutter: `clamp(1rem, 4vw, 2rem)`
- Base type: 17px / 1.7 line-height (16px under 520px)

---

## Typography

| Role | Font | Treatment |
|---|---|---|
| Display (h1) | Space Grotesk 700 | `clamp(2.1rem,6vw,3.3rem)`, tight leading, gradient text via `background-clip:text` |
| Card titles, badges | Space Grotesk 600–700 | — |
| Body | IBM Plex Sans 400–600 | 17px/1.7 |
| Labels & metadata | IBM Plex Mono 400–500 | `.68–.82rem`, uppercase, `letter-spacing .12–.22em` |

Google Fonts load:

```html
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
```

---

## Components

### Rail — sticky status bar
```html
<div class="rail">
  <span class="dot"></span>
  <b>Project Name</b> · Section 02 / 10 · Page Title
</div>
```
Frosted glass (`backdrop-filter: blur(10px)`), glowing dot colored by `--dot-color`.

### Hero
```html
<header class="hero">
  <div class="eyebrow"><span class="num">02</span> Category Label</div>
  <h1>Gradient Title</h1>
  <p class="lede">One-sentence framing with a left border.</p>
</header>
```

### Plot figure
```html
<figure class="plot">
  <svg viewBox="0 0 600 340" role="img" aria-label="...">
    <g class="tick"><!-- faint gridlines --></g>
    <g class="axis"><!-- axes --></g>
    <polyline class="curve c1" style="color:var(--poly);stroke:var(--poly)" points="..."/>
  </svg>
  <div class="legend">
    <span><i style="background:var(--poly)"></i> series label</span>
  </div>
</figure>
```
Curves self-draw on load (`.c1/.c2/.c3` stagger), disabled under `prefers-reduced-motion`. Set **both** `color` and `stroke` on curves — the glow uses `currentColor`.

### Section tag + accented h2
```html
<div class="section-tag"><b>Tutorial</b> · metadata</div>

<h2 style="--accent:var(--rat)"><span class="k">01</span>Section heading</h2>
```
Rotate `--accent` through the palette per section.

### Accent-tagged list
```html
<ul class="clean">
  <li style="--fam:var(--log)"><span class="fam">Term</span> — description.</li>
</ul>
```

### Callout
```html
<div class="callout"><p style="margin:0"><b>Key idea.</b> Summary text.</p></div>
```

### Q-card — numbered card with tap-to-reveal
```html
<div class="q" style="--qc:var(--exp)">
  <div class="q-head"><div class="q-num">7</div><div class="q-body">
    <p>Prompt text.</p></div></div>
  <details><summary>Solution</summary><div class="solution">
    <p>Hidden content.</p>
  </div></details>
</div>
```
Pure HTML `<details>` — no JS. Cycle `--qc` through the 5 accents in order for the numbered-badge rainbow.

### Next / footer nav
```html
<a class="next" href="next-page.html">
  <div><div class="lbl">Next module</div><div class="name">03 · Title</div></div>
  <div class="arrow">→</div>
</a>
```

### Index extras: stats, grid, cards
```html
<div class="stats"><div class="stat"><b>10</b> modules</div></div>

<div class="grid">
  <a class="card" style="--c:var(--trig)" href="page.html">
    <div class="card-top"><div class="badge">03</div>
      <div><h3>Card Title</h3><div class="kind">Category</div></div></div>
    <p>Description.</p>
    <div class="go">Open →</div>
  </a>
</div>
```

---

## Math (optional)

KaTeX integrates cleanly; the stylesheet includes sizing harmony rules. Load KaTeX + auto-render from a CDN and call `renderMathInElement(document.body, ...)` with `$...$` / `$$...$$` delimiters (see `starter.html` for the exact snippet, including the retry loop for deferred script loading).

---

## Accessibility

- Focus rings: 2px amber (`--exp`) outline with 3px offset on links and summaries.
- `prefers-reduced-motion` disables curve draw-in animation.
- SVG figures carry `role="img"` + `aria-label`.
- Contrast: `--ink` on `--bg` ≈ 14:1; `--ink-faint` is reserved for non-essential metadata.
- Reveal pattern uses native `<details>/<summary>` — keyboard and screen-reader friendly for free.

---

## Re-theming recipes

**New page identity (stay in system):** override the four theme knobs (`--glow`, `--dot-color`, `--g1..3`, `--next-color`).

**New brand palette:** replace the five accent hex values; every component follows automatically since nothing hardcodes hues.

**Light mode:** not provided by design — the phosphor-glow aesthetic is intrinsically dark. If you need light mode, this is the wrong system; don't fight it.

## Anti-patterns

- Assigning accent colors randomly instead of semantically.
- Using Plex Mono for body text (it's a metadata voice, not a reading voice).
- Putting more than ~5 words in mono labels.
- Skipping the `--qc` cycle on q-cards (uniform badges read as a bug once you've seen the rainbow).
- Boosting `--bg-grid` opacity above ~0.08 — the grid should be felt, not seen.
