#!/usr/bin/env python3
"""Mischa Wright Insurance Agency — static site build."""
import os, html, shutil, sys, importlib

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.abspath(os.path.join(ROOT, "..", "site"))
DOMAIN = "https://mrwrightinsures.com"

CAL = {
    "general":  "https://calendly.com/insuredwright/free15minute",
    "ltc":      "https://calendly.com/insuredwright/web-ltc-introductory-call",
    "annuity":  "https://calendly.com/insuredwright/annuity-introductory-call",
    "life":     "https://calendly.com/insuredwright/life-insurance-introductory-call",
}
GOOGLE_REVIEWS_URL = ("https://www.google.com/search?q=google+review+mischa+wright+insurance+agency"
    "&rlz=1CDGOYI_enUS777US777&hl=en-US")
RAMSEY_URL = "https://ramseytrustedltc.com"


def header(active="", depth=0):
    p = "../" * depth
    def a(link, label, key):
        cls = "active" if active == key else ""
        return f'<a class="{cls}" href="{p}{link}">{label}</a>'
    return f'''
<a class="skip-link" href="#main">Skip to main content</a>
<header class="site-header">
  <div class="bar">
    <a class="brand" href="{p}index.html">Mischa Wright<span class="brand-mark"> Insurance Agency</span></a>
    <nav class="nav" aria-label="Primary">
      {a("long-term-care-insurance.html", "Long-Term Care", "ltc")}
      <div class="dropdown">
        <button type="button" class="dropdown-trigger">Solutions</button>
        <div class="dropdown-menu" role="menu">
          <a href="{p}annuities.html" role="menuitem">Annuities</a>
          <a href="{p}life-insurance.html" role="menuitem">Life Insurance</a>
          <a href="{p}medicare.html" role="menuitem">Medicare</a>
          <a href="{p}disability-insurance.html" role="menuitem">Disability Insurance</a>
        </div>
      </div>
      {a("resources.html", "Resources", "resources")}
      {a("about.html", "About", "about")}
      {a("contact.html", "Contact", "contact")}
      <a class="btn btn-primary btn-sm" href="{p}start.html?ref=header">Start Here <span class="arrow" aria-hidden="true">→</span></a>
    </nav>
    <button class="hamburger" aria-label="Menu" aria-expanded="false" aria-controls="mobile-menu">
      <span></span><span></span><span></span>
    </button>
  </div>
  <div class="mobile-menu" id="mobile-menu" data-open="false">
    <ul>
      <li><a href="{p}index.html">Home</a></li>
      <li><a href="{p}long-term-care-insurance.html">Long-Term Care</a></li>
      <li>
        <a href="#" onclick="event.preventDefault()">Solutions</a>
        <ul class="sub">
          <li><a href="{p}annuities.html">Annuities</a></li>
          <li><a href="{p}life-insurance.html">Life Insurance</a></li>
          <li><a href="{p}medicare.html">Medicare</a></li>
          <li><a href="{p}disability-insurance.html">Disability Insurance</a></li>
        </ul>
      </li>
      <li><a href="{p}resources.html">Resources</a></li>
      <li><a href="{p}about.html">About</a></li>
      <li><a href="{p}process.html">Process</a></li>
      <li><a href="{p}faq.html">FAQ</a></li>
      <li><a href="{p}contact.html">Contact</a></li>
    </ul>
    <a class="btn btn-primary" href="{p}start.html?ref=mobile" style="width:100%">Start Here</a>
  </div>
</header>'''

def footer(depth=0):
    p = "../" * depth
    return f'''
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <div class="brand-blk">Mischa Wright<span class="brand-mark"> Insurance Agency</span></div>
        <p>Independent Long-Term Care Insurance guidance and retirement protection planning. Education-first. Nevada-based, with a licensed team serving clients nationwide.</p>
      </div>
      <div>
        <h4>Solutions</h4>
        <ul>
          <li><a href="{p}long-term-care-insurance.html">Long-Term Care</a></li>
          <li><a href="{p}annuities.html">Annuities</a></li>
          <li><a href="{p}life-insurance.html">Life Insurance</a></li>
          <li><a href="{p}medicare.html">Medicare</a></li>
          <li><a href="{p}disability-insurance.html">Disability Insurance</a></li>
        </ul>
      </div>
      <div>
        <h4>Company</h4>
        <ul>
          <li><a href="{p}about.html">About</a></li>
          <li><a href="{p}process.html">Our Process</a></li>
          <li><a href="{p}resources.html">Resources</a></li>
          <li><a href="{p}faq.html">FAQ</a></li>
          <li><a href="{p}contact.html">Contact</a></li>
        </ul>
      </div>
      <div>
        <h4>Get in touch</h4>
        <ul>
          <li><a href="mailto:Mischa@MrWrightInsures.com">Mischa@MrWrightInsures.com</a></li>
          <li><a href="tel:8583459952">858-345-9952</a></li>
          <li><a href="{p}start.html?ref=footer">Start Here</a></li>
          <li><a href="{GOOGLE_REVIEWS_URL}" target="_blank" rel="noopener">Read our Google Reviews</a></li>
        </ul>
      </div>
    </div>
    <div class="legal">
      <p>&copy; 2026 Mischa Wright Insurance Agency. All rights reserved. Insurance products are subject to underwriting, and product availability varies by state, carrier, age, and health. Guarantees are backed by the claims-paying ability of the issuing insurance company. This site does not provide tax or legal advice; consult qualified professionals for those decisions.</p>
      <p style="margin-top:12px"><a href="{p}privacy-policy.html">Privacy Policy</a> · <a href="{p}disclosures.html">Disclosures</a></p>
    </div>
  </div>
</footer>'''


def img_slot(path, alt, ratio_class="", note="", w=960, h=1200):
    """Semantic <img> with explicit dimensions (prevents layout shift)."""
    return (f'<img src="{path}" alt="{html.escape(alt)}" loading="lazy" '
            f'width="{w}" height="{h}" '
            f'onerror="this.style.visibility=\'hidden\'" />')


def render(path, title, description, body, active="", depth=0, extra_head="", schema=None):
    prefix = "../" * depth
    canonical = DOMAIN + "/" + path.replace("index.html", "").replace(".html", "")
    canonical = canonical.rstrip("/") or DOMAIN
    schema_block = ""
    if schema:
        import json as _json
        blocks = schema if isinstance(schema, list) else [schema]
        for b in blocks:
            schema_block += f'\n  <script type="application/ld+json">{_json.dumps(b, separators=(",", ":"))}</script>'
    doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(title)}</title>
  <meta name="description" content="{html.escape(description)}">
  <link rel="canonical" href="{canonical}">
  <meta property="og:title" content="{html.escape(title)}">
  <meta property="og:description" content="{html.escape(description)}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical}">
  <meta property="og:site_name" content="Mischa Wright Insurance Agency">
  <meta property="og:locale" content="en_US">
  <meta property="og:image" content="{DOMAIN}/images/og-image.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:image" content="{DOMAIN}/images/og-image.jpg">
  <meta name="theme-color" content="#12364A">
  <link rel="icon" href="{prefix}favicon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="{prefix}images/favicon-512.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,500;0,600;1,400&family=Inter:wght@400;500;600;700&display=swap">
  <link rel="stylesheet" href="{prefix}css/styles.css">
  <script>document.addEventListener('error',function(e){{if(e.target&&e.target.tagName==='IMG')e.target.style.visibility='hidden';}},true);</script>{schema_block}
  {extra_head}
</head>
<body>
{header(active, depth)}
<main id="main">
{body}
</main>
{footer(depth)}
<script src="{prefix}js/main.js" defer></script>
</body>
</html>"""
    full = os.path.join(SITE, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(doc)
    print(f"  built: {path}")


def main():
    for mod in ("pages_home", "pages_ltc", "pages_services", "pages_support", "blog_build"):
        importlib.invalidate_caches()
        m = importlib.import_module(mod)
        m.build(render=render, img_slot=img_slot, CAL=CAL,
                GR=GOOGLE_REVIEWS_URL, RAMSEY=RAMSEY_URL)
    # sitemap + robots
    write_sitemap()
    write_robots()
    print("Build complete.")


def write_sitemap():
    urls = []
    for root, _, files in os.walk(SITE):
        for f in files:
            if f.endswith(".html"):
                rel = os.path.relpath(os.path.join(root, f), SITE)
                if rel == "404.html": continue
                url = DOMAIN + "/" + rel.replace("index.html", "").replace(".html", "")
                url = url.rstrip("/") or DOMAIN
                urls.append(url)
    body = '<?xml version="1.0" encoding="UTF-8"?>\n'
    body += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for u in sorted(urls):
        body += f'  <url><loc>{u}</loc></url>\n'
    body += '</urlset>\n'
    with open(os.path.join(SITE, "sitemap.xml"), "w") as f: f.write(body)

def write_robots():
    with open(os.path.join(SITE, "robots.txt"), "w") as f:
        f.write(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")


if __name__ == "__main__":
    sys.path.insert(0, ROOT)
    main()
