"""Shared template generator for Calc 1 module pages (matches modules 01/02)."""

TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Calc 1 · __NUM__ — __TITLE__</title>

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.css">
<script defer src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.js"></script>
<script defer src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/contrib/auto-render.min.js"></script>

<style>
  :root{
    --bg:        #0a0e17;
    --bg-grid:   rgba(120,140,180,0.055);
    --surface:   #111725;
    --surface-2: #161d2e;
    --border:    rgba(150,170,210,0.12);
    --border-strong: rgba(150,170,210,0.22);

    --ink:       #e8eef7;
    --ink-soft:  #aab4c5;
    --ink-faint: #6f7b90;

    --poly:  #38bdf8;
    --rat:   #c084fc;
    --exp:   #fbbf24;
    --log:   #fb7185;
    --trig:  #34d399;

    --maxw: 780px;
    --radius: 14px;
  }

  *{ box-sizing:border-box; }
  html{ scroll-behavior:smooth; }

  body{
    margin:0;
    background:
      linear-gradient(var(--bg-grid) 1px, transparent 1px) 0 0 / 32px 32px,
      linear-gradient(90deg, var(--bg-grid) 1px, transparent 1px) 0 0 / 32px 32px,
      radial-gradient(1200px 600px at 70% -10%, __GLOW__, transparent 60%),
      var(--bg);
    color:var(--ink);
    font-family:"IBM Plex Sans", system-ui, sans-serif;
    font-size:17px;
    line-height:1.7;
    -webkit-font-smoothing:antialiased;
  }

  .katex{ font-size:1.04em; }
  .katex-display{ margin:1.3em 0; padding:.4em .2em; overflow-x:auto; overflow-y:hidden; }

  .rail{
    position:sticky; top:0; z-index:50;
    display:flex; align-items:center; gap:.6rem;
    padding:.7rem clamp(1rem,4vw,2rem);
    font-family:"IBM Plex Mono", monospace;
    font-size:.74rem; letter-spacing:.14em; text-transform:uppercase;
    color:var(--ink-faint);
    background:rgba(10,14,23,0.78);
    backdrop-filter:blur(10px);
    border-bottom:1px solid var(--border);
  }
  .rail b{ color:var(--ink-soft); font-weight:500; }
  .rail .dot{ width:7px;height:7px;border-radius:50%;background:var(__DOT__);box-shadow:0 0 10px var(__DOT__); }

  main{ max-width:var(--maxw); margin:0 auto; padding:0 clamp(1rem,4vw,2rem) 5rem; }

  .hero{ padding:3.2rem 0 1.5rem; }
  .eyebrow{
    font-family:"IBM Plex Mono", monospace;
    font-size:.8rem; letter-spacing:.22em; text-transform:uppercase;
    color:var(--exp);
    display:flex; align-items:center; gap:.75rem;
  }
  .eyebrow .num{
    font-family:"Space Grotesk", sans-serif;
    font-size:.95rem; font-weight:700;
    color:var(--bg); background:var(--exp);
    padding:.05rem .5rem; border-radius:6px; letter-spacing:.05em;
  }
  h1{
    font-family:"Space Grotesk", sans-serif;
    font-weight:700; font-size:clamp(2.1rem,6vw,3.3rem);
    line-height:1.05; letter-spacing:-0.02em;
    margin:1rem 0 .8rem;
    background:linear-gradient(100deg,var(__G1__),var(__G2__) 55%,var(__G3__));
    -webkit-background-clip:text; background-clip:text; color:transparent;
  }
  .lede{
    color:var(--ink-soft); font-size:1.08rem; max-width:60ch;
    border-left:2px solid var(--border-strong); padding-left:1rem;
  }

  figure.plot{
    margin:2rem 0 0; padding:1rem;
    background:linear-gradient(180deg,var(--surface),var(--bg));
    border:1px solid var(--border); border-radius:var(--radius);
  }
  figure.plot svg{ width:100%; height:auto; display:block; }
  .legend{
    display:flex; flex-wrap:wrap; gap:1.1rem;
    margin-top:.6rem; padding:0 .3rem;
    font-family:"IBM Plex Mono", monospace; font-size:.82rem; color:var(--ink-soft);
  }
  .legend span{ display:inline-flex; align-items:center; gap:.45rem; }
  .legend i{ width:22px; height:3px; border-radius:2px; display:inline-block; }

  .curve{ fill:none; stroke-width:2.6; stroke-linecap:round; stroke-linejoin:round;
    filter:drop-shadow(0 0 6px currentColor); }
  .axis{ stroke:rgba(160,175,205,0.35); stroke-width:1.2; }
  .tick{ stroke:rgba(160,175,205,0.18); stroke-width:1; }

  @media (prefers-reduced-motion:no-preference){
    .curve{ stroke-dasharray:1400; stroke-dashoffset:1400; animation:draw 1.6s ease forwards; }
    .curve.c2{ animation-delay:.35s; }
    .curve.c3{ animation-delay:.7s; }
    @keyframes draw{ to{ stroke-dashoffset:0; } }
  }

  .section-tag{
    display:flex; align-items:center; gap:.8rem;
    margin:3.5rem 0 1.2rem;
    font-family:"IBM Plex Mono", monospace;
    font-size:.78rem; letter-spacing:.2em; text-transform:uppercase; color:var(--ink-faint);
  }
  .section-tag::after{ content:""; flex:1; height:1px; background:var(--border); }
  .section-tag b{ color:var(--ink); font-weight:600; }

  h2{
    font-family:"Space Grotesk", sans-serif;
    font-weight:600; font-size:1.02rem; letter-spacing:.02em;
    margin:2.4rem 0 .6rem; padding-left:.9rem;
    border-left:3px solid var(--accent, var(--poly));
    color:var(--ink);
  }
  h2 .k{ color:var(--accent, var(--poly)); font-family:"IBM Plex Mono",monospace; font-size:.8rem; margin-right:.4rem; }

  p{ margin:.7rem 0; color:var(--ink); }
  strong{ color:#fff; font-weight:600; }

  ul.clean{ list-style:none; padding:0; margin:1rem 0; display:grid; gap:.55rem; }
  ul.clean li{
    padding:.7rem .9rem; background:var(--surface); border:1px solid var(--border);
    border-radius:10px; border-left:3px solid var(--fam,var(--poly));
  }
  ul.clean li .fam{ font-weight:600; color:var(--fam,var(--poly)); }

  ol.rules{ padding-left:1.2rem; margin:1rem 0; }
  ol.rules li{ margin:.4rem 0; }

  .callout{
    margin:2rem 0; padding:1.1rem 1.3rem;
    background:linear-gradient(120deg, rgba(52,211,153,0.10), rgba(56,189,248,0.06));
    border:1px solid var(--border-strong); border-radius:var(--radius);
  }
  .callout b{ color:var(--trig); }

  .q{
    margin:1rem 0; background:var(--surface); border:1px solid var(--border);
    border-radius:var(--radius); overflow:hidden;
    transition:border-color .2s ease;
  }
  .q:hover{ border-color:var(--border-strong); }
  .q-head{ display:flex; gap:.9rem; padding:1.1rem 1.2rem; }
  .q-num{
    flex:none; width:2rem; height:2rem; border-radius:8px;
    display:grid; place-items:center;
    font-family:"Space Grotesk",sans-serif; font-weight:700; font-size:.9rem;
    color:var(--bg); background:var(--qc,var(--poly));
    box-shadow:0 0 14px -2px var(--qc,var(--poly));
  }
  .q-body{ flex:1; }
  .q-body p{ margin:.2rem 0; }

  details{ border-top:1px solid var(--border); }
  summary{
    list-style:none; cursor:pointer; user-select:none;
    padding:.7rem 1.2rem .7rem 3.1rem;
    font-family:"IBM Plex Mono",monospace; font-size:.78rem;
    letter-spacing:.12em; text-transform:uppercase; color:var(--ink-faint);
    display:flex; align-items:center; gap:.5rem;
    transition:color .15s ease, background .15s ease;
  }
  summary::-webkit-details-marker{ display:none; }
  summary::before{
    content:"▸"; color:var(--qc,var(--poly)); font-size:.9rem;
    transition:transform .2s ease;
  }
  details[open] summary::before{ transform:rotate(90deg); }
  summary:hover{ color:var(--ink-soft); background:rgba(255,255,255,0.02); }
  .solution{ padding:.2rem 1.2rem 1.2rem 3.1rem; color:var(--ink-soft); }
  .solution p{ margin:.5rem 0; }

  .next{
    margin-top:3.5rem; padding:1.4rem 1.5rem;
    display:flex; align-items:center; justify-content:space-between; gap:1rem;
    background:var(--surface); border:1px solid var(--border); border-radius:var(--radius);
  }
  .next .lbl{ font-family:"IBM Plex Mono",monospace; font-size:.72rem; letter-spacing:.16em;
    text-transform:uppercase; color:var(--ink-faint); }
  .next .name{ font-family:"Space Grotesk",sans-serif; font-weight:600; font-size:1.15rem; color:var(__NEXTC__); }
  .next .arrow{ color:var(__NEXTC__); font-size:1.4rem; }

  a:focus-visible, summary:focus-visible{ outline:2px solid var(--exp); outline-offset:3px; border-radius:4px; }

  @media (max-width:520px){
    body{ font-size:16px; }
    .q-head{ padding:.9rem; }
    .solution{ padding-left:1.2rem; }
    summary{ padding-left:1.2rem; }
  }
</style>
</head>
<body>

<div class="rail">
  <span class="dot"></span>
  <b>Calculus&nbsp;1</b> · Module __NUM__ / 10 · __TITLE__
</div>

<main>

  <header class="hero">
    <div class="eyebrow"><span class="num">__NUM__</span> __EYEBROW__</div>
    <h1>__H1__</h1>
    <p class="lede">__LEDE__</p>

    <figure class="plot">
__HERO_SVG__
      <div class="legend">__LEGEND__</div>
    </figure>
  </header>

  <div class="section-tag"><b>Tutorial</b> · ~1000 words</div>

__TUTORIAL__

  <div class="callout">
    <p style="margin:0">__CALLOUT__</p>
  </div>

  <div class="section-tag"><b>Practice</b> · 20 problems · tap to reveal each solution</div>

__QUESTIONS__

  <a class="next" href="#" onclick="return false;">
    <div>
      <div class="lbl">__NEXTLBL__</div>
      <div class="name">__NEXTNAME__</div>
    </div>
    <div class="arrow">→</div>
  </a>

</main>

<script>
  window.addEventListener("DOMContentLoaded", function(){
    function render(){
      if (window.renderMathInElement){
        renderMathInElement(document.body, {
          delimiters:[
            {left:"$$", right:"$$", display:true},
            {left:"$",  right:"$",  display:false},
            {left:"\\[", right:"\\]", display:true},
            {left:"\\(", right:"\\)", display:false}
          ],
          throwOnError:false
        });
      } else {
        setTimeout(render, 60);
      }
    }
    render();
  });
</script>
</body>
</html>
"""

COLORS = ["--poly", "--rat", "--exp", "--log", "--trig"]


def build(m):
    """m: dict with module content. Writes the HTML file to outputs."""
    sections = []
    for i, (acc, title, body) in enumerate(m["sections"], start=1):
        sections.append(
            f'  <h2 style="--accent:var({acc})"><span class="k">{i:02d}</span>{title}</h2>\n{body}'
        )
    tutorial_html = "\n\n".join(sections)

    cards = []
    for i, (q, s) in enumerate(m["questions"], start=1):
        c = COLORS[(i - 1) % len(COLORS)]
        cards.append(
            f'  <div class="q" style="--qc:var({c})">\n'
            f'    <div class="q-head"><div class="q-num">{i}</div><div class="q-body">\n'
            f'      {q}</div></div>\n'
            f'    <details><summary>Solution</summary><div class="solution">\n'
            f'      {s}\n'
            f'    </div></details>\n'
            f'  </div>'
        )
    questions_html = "\n\n".join(cards)

    html = (
        TEMPLATE
        .replace("__NUM__", m["num"])
        .replace("__TITLE__", m["title"])
        .replace("__H1__", m.get("h1", m["title"]))
        .replace("__EYEBROW__", m["eyebrow"])
        .replace("__LEDE__", m["lede"])
        .replace("__GLOW__", m["glow"])
        .replace("__DOT__", m["dot"])
        .replace("__G1__", m["grad"][0])
        .replace("__G2__", m["grad"][1])
        .replace("__G3__", m["grad"][2])
        .replace("__HERO_SVG__", m["hero_svg"])
        .replace("__LEGEND__", m["legend"])
        .replace("__TUTORIAL__", tutorial_html)
        .replace("__CALLOUT__", m["callout"])
        .replace("__QUESTIONS__", questions_html)
        .replace("__NEXTLBL__", m.get("next_label", "Next module"))
        .replace("__NEXTNAME__", m["next_name"])
        .replace("__NEXTC__", m["next_color"])
    )

    path = "/mnt/user-data/outputs/" + m["file"]
    with open(path, "w") as f:
        f.write(html)
    print(f"wrote {path} ({len(html)} bytes, {len(m['questions'])} questions)")
