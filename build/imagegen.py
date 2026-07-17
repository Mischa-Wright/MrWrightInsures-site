#!/usr/bin/env python3
"""Warm Cartography — illustration system generator.
Hand-built SVG scenes rendered via Playwright to production JPG/PNG."""
import os

NAVY = "#12364A"; DEEP = "#0B2737"; GRAD_A = "#123F5A"; GRAD_B = "#1C6581"
RUST = "#A65432"; RUST_D = "#874025"
CREAM = "#F5EFE5"; CREAM_L = "#FBF8F3"; GOLD = "#E8C79A"; GOLD_D = "#D9B183"
INK2 = "#52636D"

OUT = "/home/claude/website-v2/imagegen"
os.makedirs(OUT, exist_ok=True)

GRAIN = '''
  <filter id="grain">
    <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="7" stitchTiles="stitch"/>
    <feColorMatrix type="saturate" values="0"/>
    <feComponentTransfer><feFuncA type="linear" slope="0.05"/></feComponentTransfer>
    <feComposite operator="over" in2="SourceGraphic"/>
  </filter>'''

def sky(w, h, horizon, warm=True):
    """Sky gradient from cream-light down to gold at the horizon."""
    return f'''
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{CREAM_L}"/>
      <stop offset="0.55" stop-color="{CREAM}"/>
      <stop offset="1" stop-color="{GOLD}"/>
    </linearGradient>
    <radialGradient id="sunglow" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="{GOLD}" stop-opacity="0.9"/>
      <stop offset="1" stop-color="{GOLD}" stop-opacity="0"/>
    </radialGradient>
    {GRAIN}
  </defs>
  <rect width="{w}" height="{horizon}" fill="url(#sky)"/>'''

def sun(cx, cy, r):
    return f'''
  <circle cx="{cx}" cy="{cy}" r="{r*3.2}" fill="url(#sunglow)" opacity="0.55"/>
  <circle cx="{cx}" cy="{cy}" r="{r}" fill="{RUST}"/>'''

def grain_cap(w, h):
    return f'<rect width="{w}" height="{h}" filter="url(#grain)" opacity="0.6" fill="{CREAM}" style="mix-blend-mode:multiply"/>'

def wrap(w, h, inner):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{inner}</svg>'


# ---------- HERO SCENES (960x1200, displayed 4:5) ----------

def home_hero():
    """Homepage hero: the road ahead. A path from the viewer's feet winding
    through calm hills toward a low warm sun. A small house mid-journey."""
    w, h = 960, 1200; hor = 690
    s = sky(w, h, hor)
    s += sun(660, 596, 46)
    # far hills
    s += f'<path d="M0 620 Q 240 560 480 612 T 960 596 L 960 690 L 0 690 Z" fill="{GRAD_B}" opacity="0.35"/>'
    s += f'<path d="M0 655 Q 300 600 560 648 T 960 640 L 960 700 L 0 700 Z" fill="{GRAD_B}" opacity="0.6"/>'
    # mid hills
    s += f'<path d="M0 700 Q 260 640 520 690 T 960 676 L 960 860 L 0 860 Z" fill="{GRAD_A}"/>'
    # house on mid hill
    s += f'''<g transform="translate(600 636)">
      <rect x="-26" y="0" width="52" height="38" fill="{CREAM}"/>
      <path d="M-34 2 L0 -26 L34 2 Z" fill="{RUST}"/>
      <rect x="-7" y="14" width="14" height="24" fill="{NAVY}"/>
    </g>'''
    # foreground hills
    s += f'<path d="M0 830 Q 300 760 620 820 T 960 800 L 960 1200 L 0 1200 Z" fill="{NAVY}"/>'
    s += f'<path d="M0 980 Q 320 900 640 970 T 960 950 L 960 1200 L 0 1200 Z" fill="{DEEP}"/>'
    # winding path in cream, from bottom foreground to house
    s += f'''<path d="M 430 1200
      C 470 1080 350 1010 420 930
      C 480 862 560 850 590 800
      C 612 764 606 706 600 676"
      fill="none" stroke="{CREAM}" stroke-opacity="0.9" stroke-width="30" stroke-linecap="round"/>'''
    s += f'''<path d="M 430 1200
      C 470 1080 350 1010 420 930
      C 480 862 560 850 590 800
      C 612 764 606 706 600 676"
      fill="none" stroke="{GOLD_D}" stroke-opacity="0.5" stroke-width="8" stroke-dasharray="2 26" stroke-linecap="round"/>'''
    # birds
    s += f'<path d="M300 300 q10 -10 20 0 M320 300 q10 -10 20 0" stroke="{INK2}" stroke-width="3" fill="none" opacity="0.5"/>'
    s += f'<path d="M370 340 q8 -8 16 0 M386 340 q8 -8 16 0" stroke="{INK2}" stroke-width="3" fill="none" opacity="0.4"/>'
    s += grain_cap(w, h)
    return wrap(w, h, s)


def ltc_hero():
    """LTC page: deep roots. A great sheltering tree beside a home,
    generations implied by three sizes of canopy circle."""
    w, h = 960, 1200; hor = 720
    s = sky(w, h, hor)
    s += sun(250, 622, 42)
    s += f'<path d="M0 640 Q 320 590 620 636 T 960 620 L 960 740 L 0 740 Z" fill="{GRAD_B}" opacity="0.4"/>'
    s += f'<path d="M0 690 Q 280 640 560 686 T 960 672 L 960 780 L 0 780 Z" fill="{GRAD_A}" opacity="0.85"/>'
    s += f'<path d="M0 780 Q 300 720 620 776 T 960 760 L 960 1200 L 0 1200 Z" fill="{NAVY}"/>'
    s += f'<path d="M0 1010 Q 330 950 660 1000 T 960 986 L 960 1200 L 0 1200 Z" fill="{DEEP}"/>'
    # tree: trunk + three-generation canopy
    s += f'''<g transform="translate(640 560)">
      <path d="M0 260 C -6 180 -4 120 0 60" stroke="{DEEP}" stroke-width="26" fill="none" stroke-linecap="round"/>
      <path d="M0 160 C 40 130 70 120 96 116" stroke="{DEEP}" stroke-width="14" fill="none" stroke-linecap="round"/>
      <path d="M0 120 C -44 92 -78 84 -104 82" stroke="{DEEP}" stroke-width="14" fill="none" stroke-linecap="round"/>
      <circle cx="0" cy="30" r="96" fill="{NAVY}"/>
      <circle cx="-108" cy="72" r="60" fill="{GRAD_A}"/>
      <circle cx="102" cy="98" r="44" fill="{GRAD_B}"/>
      <circle cx="30" cy="-40" r="10" fill="{RUST}" opacity="0.9"/>
    </g>'''
    # home sheltered under canopy
    s += f'''<g transform="translate(430 700)">
      <rect x="-30" y="0" width="60" height="44" fill="{CREAM}"/>
      <path d="M-40 2 L0 -30 L40 2 Z" fill="{RUST}"/>
      <rect x="-8" y="18" width="16" height="26" fill="{NAVY}"/>
      <rect x="14" y="12" width="12" height="12" fill="{GOLD}"/>
    </g>'''
    s += grain_cap(w, h)
    return wrap(w, h, s)


def annuities_hero():
    """Annuities: steady tide. Rhythmic repeated wave arcs — regular,
    dependable — under a constant sun. Income that arrives like the tide."""
    w, h = 960, 1200; hor = 560
    s = sky(w, h, hor)
    s += sun(480, 470, 44)
    # repeated wave bands, evenly spaced = regularity
    bands = [
        (560, GRAD_B, 0.35), (640, GRAD_B, 0.6), (720, GRAD_A, 0.85),
        (800, GRAD_A, 1.0), (890, NAVY, 1.0), (985, NAVY, 1.0), (1090, DEEP, 1.0),
    ]
    for i, (y, c, o) in enumerate(bands):
        off = 60 if i % 2 else 0
        s += f'''<path d="M-100 {y}
          Q {140+off} {y-46} {380+off} {y}
          T {860+off} {y} T 1340 {y}
          L 1340 1200 L -100 1200 Z" fill="{c}" opacity="{o}"/>'''
    # small boat: a household riding the steady tide
    s += f'''<g transform="translate(300 760)">
      <path d="M-44 0 Q 0 26 44 0 L 30 16 Q 0 30 -30 16 Z" fill="{CREAM}"/>
      <path d="M0 -4 L0 -54" stroke="{CREAM}" stroke-width="6"/>
      <path d="M0 -54 C 20 -46 30 -30 28 -12 L 2 -10 Z" fill="{RUST}"/>
    </g>'''
    s += grain_cap(w, h)
    return wrap(w, h, s)


def life_hero():
    """Life insurance: the canopy. Concentric sheltering arcs over a small
    cluster of homes — protection over the family."""
    w, h = 960, 1200; hor = 820
    s = sky(w, h, hor)
    s += sun(480, 330, 40)
    # concentric protective arcs
    for r, col, op, sw in [(470, GRAD_B, 0.28, 30), (390, GRAD_B, 0.45, 32), (310, GRAD_A, 0.7, 34), (232, NAVY, 0.9, 36)]:
        s += f'<path d="M {480-r} 820 A {r} {r} 0 0 1 {480+r} 820" fill="none" stroke="{col}" stroke-opacity="{op}" stroke-width="{sw}" stroke-linecap="round"/>'
    # ground
    s += f'<path d="M0 820 Q 240 790 480 812 T 960 806 L 960 1200 L 0 1200 Z" fill="{NAVY}"/>'
    s += f'<path d="M0 1010 Q 320 970 640 1002 T 960 992 L 960 1200 L 0 1200 Z" fill="{DEEP}"/>'
    # family of homes under the arcs
    for dx, sc in [(-130, 0.8), (0, 1.15), (130, 0.9)]:
        s += f'''<g transform="translate({480+dx} 796) scale({sc})">
          <rect x="-26" y="0" width="52" height="38" fill="{CREAM}"/>
          <path d="M-34 2 L0 -26 L34 2 Z" fill="{RUST}"/>
          <rect x="-7" y="16" width="14" height="22" fill="{NAVY}"/>
        </g>'''
    # two small trees
    s += f'<g transform="translate(250 812)"><path d="M0 0 L0 -34" stroke="{DEEP}" stroke-width="8"/><circle cy="-52" r="26" fill="{GRAD_A}"/></g>'
    s += f'<g transform="translate(716 806)"><path d="M0 0 L0 -28" stroke="{DEEP}" stroke-width="7"/><circle cy="-44" r="22" fill="{GRAD_B}"/></g>'
    s += grain_cap(w, h)
    return wrap(w, h, s)


def medicare_hero():
    """Medicare: the lighthouse. Navigation through complex waters —
    guidance from the licensed team."""
    w, h = 960, 1200; hor = 700
    s = sky(w, h, hor)
    s += sun(230, 600, 38)
    # sea
    s += f'<path d="M0 700 L960 700 L960 1200 L0 1200 Z" fill="{GRAD_A}"/>'
    s += f'<path d="M-80 780 Q 160 750 400 776 T 880 772 T 1360 772 L 1360 1200 L -80 1200 Z" fill="{NAVY}"/>'
    s += f'<path d="M-80 960 Q 200 924 480 952 T 1040 948 L 1040 1200 L -80 1200 Z" fill="{DEEP}"/>'
    # headland
    s += f'<path d="M520 700 Q 700 610 960 640 L 960 900 L 560 880 Q 520 780 520 700 Z" fill="{DEEP}"/>'
    # lighthouse
    s += f'''<g transform="translate(760 620)">
      <path d="M-30 0 L30 0 L20 -150 L-20 -150 Z" fill="{CREAM}"/>
      <path d="M-30 -30 L30 -30 L27 -62 L-27 -62 Z" fill="{RUST}"/>
      <path d="M-24 -96 L24 -96 L22 -120 L-22 -120 Z" fill="{RUST}"/>
      <rect x="-16" y="-150" width="32" height="-0" fill="{NAVY}"/>
      <rect x="-16" y="-176" width="32" height="26" fill="{NAVY}"/>
      <circle cx="0" cy="-163" r="9" fill="{GOLD}"/>
      <path d="M-14 -176 L0 -196 L14 -176 Z" fill="{RUST_D}"/>
      <path d="M-9 -163 L-150 -120 L-150 -206 Z" fill="{GOLD}" opacity="0.4"/>
    </g>'''
    s += grain_cap(w, h)
    return wrap(w, h, s)


def disability_hero():
    """Disability: the bridge. Income carries a household across the gap
    when work stops. A steady bridge spanning a river valley."""
    w, h = 960, 1200; hor = 640
    s = sky(w, h, hor)
    s += sun(700, 540, 42)
    # far banks
    s += f'<path d="M0 640 Q 200 600 340 636 L 340 900 L 0 900 Z" fill="{GRAD_A}"/>'
    s += f'<path d="M620 636 Q 800 596 960 628 L 960 900 L 620 900 Z" fill="{GRAD_A}"/>'
    # river through the gap
    s += f'<path d="M340 900 L340 660 Q 480 700 620 660 L620 900 Z" fill="{GRAD_B}" opacity="0.7"/>'
    # near banks
    s += f'<path d="M0 860 Q 260 810 400 856 L 400 1200 L 0 1200 Z" fill="{NAVY}"/>'
    s += f'<path d="M560 852 Q 740 806 960 850 L 960 1200 L 560 1200 Z" fill="{NAVY}"/>'
    s += f'<path d="M0 1060 L 960 1040 L 960 1200 L 0 1200 Z" fill="{DEEP}"/>'
    # bridge deck + arch + piers
    s += f'<rect x="140" y="600" width="680" height="22" rx="10" fill="{DEEP}"/>'
    s += f'<path d="M200 622 Q 480 480 760 622" fill="none" stroke="{RUST}" stroke-width="18" stroke-linecap="round"/>'
    for x in (296, 388, 480, 572, 664):
        # suspender from arch to deck
        s += f'<line x1="{x}" y1="{560 - abs(480-x)*0.22:.0f}" x2="{x}" y2="600" stroke="{RUST}" stroke-width="8" opacity="0.85"/>'
    s += f'<rect x="216" y="622" width="26" height="180" fill="{DEEP}"/>'
    s += f'<rect x="716" y="622" width="26" height="176" fill="{DEEP}"/>'
    # small figure-scale house crossing (kept as house = household)
    s += f'''<g transform="translate(480 586)">
      <rect x="-16" y="0" width="32" height="20" fill="{CREAM}"/>
      <path d="M-21 1 L0 -15 L21 1 Z" fill="{GOLD_D}"/>
    </g>'''
    s += grain_cap(w, h)
    return wrap(w, h, s)


# ---------- BLOG THUMBS (1280x720) ----------

def thumb_base(hor):
    return sky(1280, 720, hor)

def ltc_covers_thumb():
    """What LTC covers: umbrella over the home cluster."""
    w, h = 1280, 720; s = thumb_base(470)
    s += sun(1010, 160, 34)
    s += f'<path d="M0 470 Q 320 420 640 460 T 1280 450 L 1280 720 L 0 720 Z" fill="{NAVY}"/>'
    s += f'<path d="M0 590 Q 360 550 720 584 T 1280 574 L 1280 720 L 0 720 Z" fill="{DEEP}"/>'
    # big sheltering umbrella
    s += f'''<g transform="translate(420 300)">
      <path d="M-190 0 A 190 190 0 0 1 190 0 Z" fill="{RUST}"/>
      <path d="M-190 0 A 190 190 0 0 1 -63 -179 A 63 190 0 0 0 -63 0 Z" fill="{RUST_D}" opacity="0.5"/>
      <path d="M63 0 A 63 190 0 0 1 63 -179 A 190 190 0 0 1 190 0 Z" fill="{RUST_D}" opacity="0.5"/>
      <line x1="0" y1="0" x2="0" y2="150" stroke="{DEEP}" stroke-width="10"/>
      <path d="M0 150 q 0 26 26 24" stroke="{DEEP}" stroke-width="10" fill="none" stroke-linecap="round"/>
    </g>'''
    # homes under it
    for dx, sc in [(300, 0.9), (430, 1.2), (560, 0.95)]:
        s += f'''<g transform="translate({dx} 452) scale({sc})">
          <rect x="-24" y="0" width="48" height="34" fill="{CREAM}"/>
          <path d="M-31 1 L0 -23 L31 1 Z" fill="{GOLD_D}"/>
          <rect x="-6" y="14" width="12" height="20" fill="{NAVY}"/>
        </g>'''
    s += grain_cap(w, h)
    return wrap(w, h, s)

def med_vs_ltc_thumb():
    """Medicare vs LTC: two hills, two colors, one valley between —
    mirrors the site's navy/rust compare table."""
    w, h = 1280, 720; s = thumb_base(430)
    s += sun(640, 150, 34)
    s += f'<path d="M0 720 L0 430 Q 240 300 560 430 Q 620 460 640 470 L 640 720 Z" fill="{NAVY}"/>'
    s += f'<path d="M1280 720 L1280 430 Q 1040 300 720 430 Q 660 460 640 470 L 640 720 Z" fill="{RUST}"/>'
    s += f'<path d="M0 600 Q 320 560 640 592 T 1280 584 L 1280 720 L 0 720 Z" fill="{DEEP}"/>'
    # flags on each summit
    s += f'<g transform="translate(300 368)"><line y2="-64" stroke="{CREAM}" stroke-width="8"/><path d="M0 -64 L46 -50 L0 -36 Z" fill="{CREAM}"/></g>'
    s += f'<g transform="translate(980 368)"><line y2="-64" stroke="{CREAM}" stroke-width="8"/><path d="M0 -64 L46 -50 L0 -36 Z" fill="{CREAM}"/></g>'
    s += grain_cap(w, h)
    return wrap(w, h, s)

def when_to_buy_thumb():
    """When to buy: the sun's arc across the sky — the planning window.
    Sun shown mid-arc, past positions ghosted, later positions fading."""
    w, h = 1280, 720; s = thumb_base(520)
    # arc path
    s += f'<path d="M140 520 A 520 470 0 0 1 1140 520" fill="none" stroke="{GOLD_D}" stroke-width="4" stroke-dasharray="3 18" opacity="0.9"/>'
    # sun positions: early ghosts, present solid rust, later fading navy
    pts = [(266, 342, 20, GOLD_D, 0.55), (420, 210, 24, GOLD_D, 0.75),
           (640, 152, 40, RUST, 1.0),
           (860, 210, 24, INK2, 0.5), (1014, 342, 20, INK2, 0.35)]
    for cx, cy, r, col, op in pts:
        s += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{col}" opacity="{op}"/>'
    s += f'<circle cx="640" cy="152" r="118" fill="url(#sunglow)" opacity="0.5"/>'
    s += f'<path d="M0 520 Q 320 470 640 508 T 1280 498 L 1280 720 L 0 720 Z" fill="{NAVY}"/>'
    s += f'<path d="M0 620 Q 360 580 720 612 T 1280 602 L 1280 720 L 0 720 Z" fill="{DEEP}"/>'
    s += f'''<g transform="translate(640 494)">
      <rect x="-24" y="0" width="48" height="34" fill="{CREAM}"/>
      <path d="M-31 1 L0 -23 L31 1 Z" fill="{RUST}"/>
    </g>'''
    s += grain_cap(w, h)
    return wrap(w, h, s)

def cost_thumb():
    """Cost: layered strata — the five factors stacking into a premium.
    A cross-section hillside of five labeled-by-color layers."""
    w, h = 1280, 720; s = thumb_base(300)
    s += sun(1040, 150, 32)
    layers = [(300, GRAD_B, 0.45), (384, GRAD_B, 0.75), (468, GRAD_A, 0.95), (552, NAVY, 1.0), (636, DEEP, 1.0)]
    for y, c, o in layers:
        s += f'<path d="M0 {y} Q 320 {y-40} 640 {y-6} T 1280 {y-14} L 1280 720 L 0 720 Z" fill="{c}" opacity="{o}"/>'
    # one rust coin embedded = the premium
    s += f'<circle cx="420" cy="400" r="46" fill="{RUST}"/>'
    s += f'<circle cx="420" cy="400" r="46" fill="none" stroke="{CREAM}" stroke-width="5" stroke-dasharray="4 12" opacity="0.8"/>'
    s += grain_cap(w, h)
    return wrap(w, h, s)

def trad_vs_hybrid_thumb():
    """Traditional vs hybrid vs annuity: three paths to one horizon."""
    w, h = 1280, 720; s = thumb_base(430)
    s += sun(640, 200, 38)
    s += f'<path d="M0 430 Q 320 380 640 420 T 1280 410 L 1280 720 L 0 720 Z" fill="{NAVY}"/>'
    s += f'<path d="M0 600 Q 360 560 720 592 T 1280 582 L 1280 720 L 0 720 Z" fill="{DEEP}"/>'
    # three converging paths
    s += f'<path d="M220 720 C 320 620 520 520 620 434" fill="none" stroke="{CREAM}" stroke-width="22" stroke-linecap="round" opacity="0.95"/>'
    s += f'<path d="M640 720 C 640 620 640 520 640 430" fill="none" stroke="{RUST}" stroke-width="22" stroke-linecap="round"/>'
    s += f'<path d="M1060 720 C 960 620 760 520 660 434" fill="none" stroke="{GOLD_D}" stroke-width="22" stroke-linecap="round" opacity="0.95"/>'
    s += grain_cap(w, h)
    return wrap(w, h, s)


# ---------- OG IMAGE (1200x630) + FAVICON ----------

def og_image():
    w, h = 1200, 630; hor = 470
    s = sky(w, h, hor)
    s += sun(880, 380, 40)
    s += f'<path d="M0 400 Q 300 350 600 392 T 1200 380 L 1200 630 L 0 630 Z" fill="{GRAD_A}" opacity="0.5"/>'
    s += f'<path d="M0 470 Q 300 420 620 462 T 1200 450 L 1200 630 L 0 630 Z" fill="{NAVY}"/>'
    s += f'<path d="M0 540 Q 340 500 680 532 T 1200 524 L 1200 630 L 0 630 Z" fill="{DEEP}"/>'
    s += f'''<text x="80" y="180" font-family="Georgia, 'Times New Roman', serif" font-size="64" fill="{NAVY}" font-weight="500">Mischa Wright</text>
    <text x="80" y="240" font-family="Georgia, serif" font-size="44" font-style="italic" fill="{RUST}">Insurance Agency</text>
    <text x="80" y="308" font-family="Helvetica, Arial, sans-serif" font-size="25" fill="{INK2}" letter-spacing="1">Long-Term Care Planning, Explained in Plain English</text>'''
    s += grain_cap(w, h)
    return wrap(w, h, s)

def favicon():
    """Monogram mark: horizon-in-circle with rust sun."""
    w = h = 512
    s = f'''
  <defs>
    <linearGradient id="fsky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{CREAM_L}"/><stop offset="1" stop-color="{GOLD}"/>
    </linearGradient>
    <clipPath id="round"><circle cx="256" cy="256" r="256"/></clipPath>
  </defs>
  <g clip-path="url(#round)">
    <rect width="512" height="512" fill="url(#fsky)"/>
    <circle cx="330" cy="222" r="58" fill="{RUST}"/>
    <path d="M0 300 Q 128 250 256 288 T 512 276 L 512 512 L 0 512 Z" fill="{NAVY}"/>
    <path d="M0 400 Q 150 362 300 392 T 512 384 L 512 512 L 0 512 Z" fill="{DEEP}"/>
  </g>'''
    return wrap(w, h, s)


SCENES = {
    "home-hero": (home_hero, "site/images/generated/home-hero.jpg"),
    "ltc-hero": (ltc_hero, "site/images/generated/ltc-hero.jpg"),
    "annuities-hero": (annuities_hero, "site/images/generated/annuities-hero.jpg"),
    "life-hero": (life_hero, "site/images/generated/life-hero.jpg"),
    "medicare-hero": (medicare_hero, "site/images/generated/medicare-hero.jpg"),
    "disability-hero": (disability_hero, "site/images/generated/disability-hero.jpg"),
    "ltc-covers-thumb": (ltc_covers_thumb, "site/images/blog/ltc-covers-thumb.jpg"),
    "medicare-vs-ltc-thumb": (med_vs_ltc_thumb, "site/images/blog/medicare-vs-ltc-thumb.jpg"),
    "when-to-buy-thumb": (when_to_buy_thumb, "site/images/blog/when-to-buy-thumb.jpg"),
    "cost-thumb": (cost_thumb, "site/images/blog/cost-thumb.jpg"),
    "traditional-vs-hybrid-thumb": (trad_vs_hybrid_thumb, "site/images/blog/traditional-vs-hybrid-thumb.jpg"),
    "og-image": (og_image, "site/images/og-image.jpg"),
    "favicon": (favicon, "site/favicon.svg"),
}

if __name__ == "__main__":
    for name, (fn, _) in SCENES.items():
        svg = fn()
        with open(os.path.join(OUT, name + ".svg"), "w") as f:
            f.write(svg)
        print("svg:", name)
