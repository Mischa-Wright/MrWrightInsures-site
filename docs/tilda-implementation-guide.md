# Tilda Implementation Guide
Mischa Wright Insurance Agency | mrwrightinsures.com

## How to use this guide
The `site/` folder is a working prototype. Open any page in a browser to see exactly what to recreate. This guide maps each section to Tilda blocks and lists the custom code you need.

## Global setup (do once)

### Site settings
- Fonts: Lora (headings) + Inter (body) via Tilda's Google Fonts settings
- Colors: add to Tilda palette: navy #12364A, deep navy #0B2737, rust #A65432, cream #F5EFE5, light cream #FBF8F3, text #17252E, secondary #52636D, border #DED6CA
- Primary button style: gradient `linear-gradient(135deg, #123F5A 0%, #1C6581 100%)`, white text, fully rounded (999px radius)

### Header (T228 or Zero Block, set as global)
- One line: brand left, nav center-right, Start Here button far right
- Brand: "Mischa Wright" (Lora) + " Insurance Agency" in rust italic
- Nav: Long-Term Care | Solutions (dropdown: Annuities, Life Insurance, Medicare, Disability Insurance) | Resources | About | Contact
- No "Home" item (brand links home). No Process/FAQ in nav (footer only)
- Start Here button: gradient style, links to /start
- Mobile: hamburger; Start Here as full-width button at bottom of opened menu

### Footer (global)
4 columns: brand+positioning / Solutions links / Company links / Contact + Google Reviews link. One concise legal paragraph + Privacy/Disclosures links. Copy verbatim from prototype footer.

### Custom code (Site Settings -> Custom Code, before </body>)
Paste the contents of `js/main.js`. It handles: service parameter persistence (?service=), hidden-field prefill (source_page, referrer, UTMs), and form validation. Tilda handles its own form submission; keep the persistence code.

## Page-by-page

### Home (/)
1. Hero: Zero Block, 2 columns. Eyebrow + H1 "Long-Term Care Planning, Explained in Plain English." + lede + Start Here button. Right: hero image with "RamseyTrusted LTC Pro" rust pill overlaid top-right
2. Trust strip: T123 list-style with 5 items, rust dot separators
3. Advisor block (HIGH on page): 2 columns; headshot with rust offset frame (Zero Block shape offset 12px behind photo); bio copy with CLTC pill; buttons: About + Google Reviews
4. Dark statement: full-width navy section, centered large serif statement + HHS stat
5. Services: LTC lead card (full-width, left gradient bar, "Flagship specialty" tag) then 2-col Annuities/Life cards, then Medicare + Disability as plain text rows with rust dots
6. Independent advantage: 2-col split, copy left, 3 numbered steps right (rust top borders)
7. Google Reviews band: white card, G icon, stars, "Read our Google Reviews" button (opens new tab)
8. Recent guides: 3 post cards
9. FAQ preview: 4 items, native accordion (T509 or Zero Block details style)
10. CTA band: navy gradient with soft rust radial glows, white "Start Here" button

### Start Here (/start)
Centered H1 "What would you like help with?" then chooser: LTC card full-width navy ("Our flagship specialty"), then 5 cards (Annuities, Life, Medicare, Disability, Not sure). Links carry ?service= parameters:
- LTC -> /long-term-care-insurance?service=ltc
- Annuities -> /annuities?service=annuities
- Life -> /life-insurance?service=life
- Medicare -> /medicare?service=medicare
- Disability -> /disability-insurance?service=disability
- Not sure -> /contact?service=general

### Long-Term Care (/long-term-care-insurance)
Follow prototype order: hero (CTA = LTC Calendly) / section-nav pill row / what-it-covers 6 definitions / Medicare-vs-LTC comparison (two-color table: navy vs rust headers) / policy types comparison / policy design 6 definitions + elimination-period 4-phase timeline / underwriting split with pre-screening callout / 3-step process / 5-item FAQ / CTA band.

### Annuities, Life Insurance
Per prototype. CTAs: "Book an Annuity Call" -> annuity Calendly; "Request a Life Insurance Quote" -> life Calendly.

### Medicare (/medicare) - FORM ONLY, NO CALENDLY
Hero + 2-col: checklist left, Tilda form right. Hidden field product_interest=Medicare. CTA "Request Medicare Help".

### Disability (/disability-insurance) - FORM ONLY, NO CALENDLY
Hero (button jumps to #quote-form) / definitions grid (8 provisions) / business-owner section / form. Hidden field product_interest=Disability Insurance.

### About, Process, FAQ, Contact, Resources, articles, Privacy, Disclosures, 404
Copy verbatim from prototype HTML. Contact page includes all four Calendly links plus note directing Medicare/Disability to their forms.

## Calendly links (exact)
- General: https://calendly.com/insuredwright/free15minute
- LTC: https://calendly.com/insuredwright/web-ltc-introductory-call
- Annuity: https://calendly.com/insuredwright/annuity-introductory-call
- Life: https://calendly.com/insuredwright/life-insurance-introductory-call
- Medicare: NONE (form only). Disability: NONE (form only).

## SEO per page
Each prototype page has its title, meta description, and canonical in the <head>. Copy into Tilda page settings. Upload sitemap handling is automatic in Tilda; submit domain in Search Console after launch.
