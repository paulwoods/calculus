# Page generator

`template_gen.py` is the Python generator used to stamp out the Calculus 1 course
pages. It holds the full page template (inlined CSS) and a `build(m)` function
that takes a content dict and writes a finished HTML file.

Content dict shape:

```python
M = {
  "num": "03", "file": "output.html",
  "title": "...", "h1": "...",          # h1 optional, defaults to title
  "eyebrow": "...", "lede": "...",
  "glow": "rgba(...)", "dot": "--trig",  # theme knobs
  "grad": ("--trig", "--poly", "--exp"),
  "hero_svg": "<svg>...</svg>", "legend": "<span>...</span>",
  "sections": [("--accent-var", "Heading", "<p>body html</p>"), ...],
  "callout": "<b>...</b> ...",
  "questions": [("<p>question html</p>", "<p>solution html</p>"), ...],
  "next_name": "...", "next_color": "--exp",
  "next_label": "Next module",          # optional
}
```

Q-card accent colors cycle automatically (poly → rat → exp → log → trig).
Edit the output path inside `build()` for your project.

Note: the generator inlines the stylesheet for fully self-contained pages.
If you prefer the external `css/graph-night.css`, swap the `<style>` block in
TEMPLATE for a `<link>` tag.
