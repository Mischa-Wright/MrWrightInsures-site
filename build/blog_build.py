"""Blog posts - 5 launch articles."""
import os, html

def build(render, img_slot, CAL, GR, RAMSEY):
    for post in POSTS:
        _post(render, img_slot, CAL, post)


def _post(render, img_slot, CAL, post):
    slug, title, cat, updated, read_time, hero_alt, body_html, cta_key = post
    others = [(s2, t2) for (s2, t2, *_rest) in POSTS if s2 != slug][:3]
    related_links = "".join(
        f'<p style="margin: 6px 0;"><a href="{s2}.html">{t2}</a></p>' for s2, t2 in others)
    cta_link = CAL.get(cta_key, CAL["general"])
    cta_label = {"ltc": "Book an LTC Intro Call", "general": "Book a 15-Minute Call"}.get(cta_key, "Book a 15-Minute Call")

    body = f'''
<section class="article-hero alt">
  <div class="wrap-mid">
    <span class="eyebrow">{cat}</span>
    <h1>{title}</h1>
    <div class="meta">
      <span>By Mischa Wright, CLTC&reg;</span>
      <span>&middot;</span>
      <span>Updated {updated}</span>
      <span>&middot;</span>
      <span>{read_time} min read</span>
    </div>
  </div>
</section>

<article class="article-body">
  {body_html}

  <div class="callout" style="margin-top: 48px;">
    <p style="margin: 0; font-weight: 600;">Ready to talk it through?</p>
    <p style="margin: 8px 0 16px; color: var(--ink-2);">A short conversation is the fastest way to see whether the ideas here fit your situation.</p>
    <a class="btn btn-primary" href="{cta_link}" target="_blank" rel="noopener">{cta_label} <span class="arrow" aria-hidden="true">&rarr;</span></a>
  </div>

  <nav class="related" aria-label="Related guides" style="margin-top: 40px; padding-top: 24px; border-top: 1px solid var(--border);">
    <p style="font-weight: 600; margin-bottom: 10px;">Keep reading</p>
    {related_links}
  </nav>

  <div class="sources">
    <p><strong>Sources & further reading.</strong> U.S. Department of Health and Human Services, LongTermCare.gov (care statistics and definitions). Genworth Cost of Care Survey (annual industry cost benchmark). Medicare.gov (Medicare coverage rules). National Association of Insurance Commissioners, A Shopper&rsquo;s Guide to Long-Term Care Insurance. Illustrative pricing in this article is for education only and does not represent a quote for any specific person or policy.</p>
  </div>
</article>
'''
    schema = [
      {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "author": {"@type": "Person", "name": "Mischa Wright", "honorificSuffix": "CLTC"},
        "publisher": {"@type": "Organization", "name": "Mischa Wright Insurance Agency",
                      "logo": {"@type": "ImageObject", "url": "https://mrwrightinsures.com/images/favicon-512.png"}},
        "datePublished": "2026-06-15",
        "dateModified": "2026-07-04",
        "image": f"https://mrwrightinsures.com/images/blog/{THUMBS[slug]}",
        "mainEntityOfPage": f"https://mrwrightinsures.com/blog/{slug}",
        "articleSection": cat
      },
      {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
          {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://mrwrightinsures.com"},
          {"@type": "ListItem", "position": 2, "name": "Resources", "item": "https://mrwrightinsures.com/resources"},
          {"@type": "ListItem", "position": 3, "name": title, "item": f"https://mrwrightinsures.com/blog/{slug}"}
        ]
      }
    ]
    render(path=f"blog/{slug}.html",
        schema=schema,
        title=f"{title} | Mischa Wright Insurance Agency",
        description=(title + ". Education-first Long-Term Care planning guidance from Mischa Wright, CLTC.")[:300],
        body=body, active="resources", depth=1)


# --------- Post bodies ---------

_WHAT_LTC_COVERS = '''
<p class="lede">Long-Term Care Insurance is a specific type of insurance that pays for the ongoing care most families eventually need and Medicare will not cover. Because that description is broad, this guide walks through exactly what a modern policy pays for, where it pays, and where it stops.</p>

<h2>The benefit that actually shows up as money</h2>
<p>A Long-Term Care policy pays a monthly benefit up to a contracted maximum, drawn from a benefit pool of dollars or years. You use that benefit toward qualifying care expenses. Once the elimination period is satisfied, the carrier pays either the actual monthly cost or the monthly maximum, whichever is less.</p>

<h2>What triggers benefits</h2>
<p>In most contracts, benefits become payable when either of these is true and expected to last at least 90 days:</p>
<ul>
  <li>You cannot perform at least two of the six activities of daily living (bathing, dressing, eating, transferring, toileting, and continence).</li>
  <li>You need substantial supervision because of cognitive impairment such as dementia.</li>
</ul>
<p>A licensed practitioner or care coordinator documents the trigger.</p>

<h2>Where the money can be used</h2>
<p>Modern LTC insurance is portable across care settings. That flexibility matters, because most families end up using more than one type of care over the course of a claim.</p>

<h3>Home care</h3>
<p>The most common care setting today. Policies pay home care aides, home health services, and in some cases modest home modifications so care can be delivered where you live.</p>

<h3>Assisted living</h3>
<p>Monthly benefits pay toward residence in an assisted living community when help with daily activities is needed but round-the-clock nursing is not.</p>

<h3>Memory care communities</h3>
<p>Specialized cognitive care communities. This is a setting where LTC coverage matters most, because Medicare covers essentially none of this care.</p>

<h3>Skilled nursing</h3>
<p>Long stays in a skilled nursing facility, once short-term Medicare coverage ends and the care becomes custodial rather than rehabilitative.</p>

<h3>Adult day services</h3>
<p>Structured daytime care that lets a working family caregiver keep their job.</p>

<h2>Extras many policies include</h2>
<ul>
  <li>Care coordination through a nurse who helps a family navigate providers and paperwork at the moment they most need it.</li>
  <li>Caregiver training for a family member who wants to help with care at home.</li>
  <li>Home modification allowances (grab bars, ramps, stair lifts) in some contracts, subject to contract limits.</li>
  <li>Respite care so a family caregiver can rest.</li>
</ul>

<h2>Where coverage stops</h2>
<p>An LTC policy is not a general medical policy. It does not cover:</p>
<ul>
  <li>Hospital or physician bills; those belong to health insurance and Medicare.</li>
  <li>Prescription drugs.</li>
  <li>Care that occurs before the elimination period is satisfied (this is the deductible).</li>
  <li>Care beyond the contract&rsquo;s monthly maximum or benefit pool.</li>
</ul>
<p>Understanding this boundary is part of understanding why an LTC policy sits next to health insurance rather than replacing it.</p>

<h2>Bringing it back to the plan</h2>
<p>The policy&rsquo;s job is to fund care so that the choices about how, where, and who provides it can stay with you and your family. That is the whole point.</p>
'''

_MEDICARE_VS_LTC = '''
<p class="lede">One of the most common and expensive misunderstandings in retirement planning is the assumption that Medicare will pay for long-term care. It will not, at least not in the way most families expect. Here is the honest split.</p>

<h2>Medicare does two things well</h2>
<p>Medicare is a federal health insurance program for people age 65 and older, and for certain younger people with disabilities. It covers:</p>
<ul>
  <li>Hospital care and physician services.</li>
  <li>Short-term skilled care after a qualifying hospital stay of at least three days. Coverage runs up to 100 days per benefit period, with days 1&ndash;20 fully paid and days 21&ndash;100 subject to a substantial daily copay.</li>
  <li>Limited home health for medically necessary skilled care.</li>
  <li>Hospice care.</li>
</ul>

<h2>What Medicare does not do</h2>
<p>Medicare was not designed to pay for the ongoing custodial care that most long-term care claims involve. That is help with the activities of daily living: bathing, dressing, eating, transferring, and supervision for cognitive decline. Whether the care is delivered at home, in an assisted living community, in memory care, or in a skilled nursing facility, Medicare will not fund it once the short-term skilled window closes.</p>

<h2>Where the confusion comes from</h2>
<p>Two words carry a lot of weight in this space: <strong>skilled</strong> and <strong>custodial</strong>.</p>
<ul>
  <li><strong>Skilled</strong> care is what a licensed clinician provides: wound care, IV therapy, physical rehabilitation. Medicare covers a limited amount of this after a hospital stay.</li>
  <li><strong>Custodial</strong> care is the ongoing help with daily living that most long-term care actually is. Medicare does not cover this.</li>
</ul>
<p>When the short-term skilled window closes and care continues, the bill shifts entirely to the family (or, in some cases, Medicaid after assets have been spent down).</p>

<h2>What Long-Term Care Insurance covers</h2>
<p>Long-Term Care Insurance was designed specifically for this custodial care. Policies fund care at home, in assisted living, in memory care, or in skilled nursing, once the trigger conditions are met. Many contracts also include care coordination services that help a family navigate providers and paperwork.</p>

<h2>The clean split</h2>
<p>Think of it this way: Medicare covers the medical side (hospital, doctor, short-term rehab). Long-Term Care Insurance covers the daily-living side once the medical piece is done. Both belong in a real retirement plan; they do different jobs.</p>

<h2>Medicaid is a different program</h2>
<p>Medicaid does fund custodial long-term care, but it is a needs-based program that requires spending down assets first. Rules vary by state and are strict. Partnership-qualified Long-Term Care policies, available in most states, provide additional Medicaid asset protection if benefits are ever exhausted. Availability and terms vary by state.</p>

<h2>What to do with this</h2>
<p>If your retirement plan assumes Medicare will handle a long-term care event, it does not. Build the coverage before you need it, or plan for the family to self-fund it, or plan for Medicaid eligibility. All three are legitimate. Assuming Medicare will do the job is the plan that fails.</p>
'''

_WHEN_TO_BUY = '''
<p class="lede">The right time to buy Long-Term Care Insurance is when three things are true at once: you are healthy enough to qualify, young enough that pricing is reasonable, and the coverage would meaningfully improve your plan. That window opens in your fifties for most people and gradually closes with age.</p>

<h2>Why age matters</h2>
<p>LTC premiums are based on age at application. The younger you are when you apply, the lower the annual premium, and the longer the coverage compounds if you have chosen inflation protection. Waiting a year rarely feels expensive in the moment. Waiting five or ten years often is.</p>
<p>As an illustrative example only, a healthy 55-year-old applying for a hybrid life/LTC design might see meaningfully lower premiums than the same coverage taken at 65. Numbers vary by carrier, state, and design; the point is directional, not a quote.</p>

<h2>Why health matters more</h2>
<p>Underwriting is the real gate, not price. LTC coverage is medically underwritten. Underwriters are not asking whether you might get sick, they are asking how likely you are to need extended help with daily living.</p>
<p>Well-managed conditions (blood pressure, cholesterol, controlled diabetes) are routinely insurable. Memory and cognitive concerns are the most sensitive area, and a dementia diagnosis generally makes traditional coverage unavailable.</p>
<p>Health changes tend to be sudden, not gradual. The window from &ldquo;fully insurable&rdquo; to &ldquo;partially insurable&rdquo; can be a single doctor&rsquo;s visit.</p>

<h2>The three-question filter</h2>
<p>Not everyone needs LTC insurance, and this guide is not going to pretend otherwise. Three questions help identify whether the coverage fits.</p>

<h3>Question 1: What would a two-to-five-year care event cost your family?</h3>
<p>Not just the money. The disruption. The decisions someone else would have to make. A meaningful LTC design typically covers most or all of that cost.</p>

<h3>Question 2: What are the honest funding sources today?</h3>
<p>Retirement accounts, pension income, home equity, family support. If a $200,000 to $500,000 care event would meaningfully change the retirement plan for the surviving spouse, insurance is worth serious consideration.</p>

<h3>Question 3: What is your health picture?</h3>
<p>If it is generally good and your family history is reasonable, you have optionality. Use it now, while you have it.</p>

<h2>The typical planning windows</h2>
<h3>Mid-50s to early-60s: the sweet spot</h3>
<p>Pricing is reasonable, health tends to be good, and the design has time to compound with inflation protection. Most people who plan well plan in this window.</p>
<h3>Mid-60s: still workable, more targeted</h3>
<p>Pricing is meaningfully higher and some designs get more expensive. Hybrid life/LTC often looks better than traditional at this age because premiums are contractually level in many designs. Still worth exploring.</p>
<h3>Late-60s and beyond: fewer options, still not zero</h3>
<p>Traditional coverage becomes harder to obtain and often less economical. Hybrid designs, asset-based LTC, and annuity-based strategies with simplified underwriting are typically the next place to look.</p>

<h2>The single most useful thing to do first</h2>
<p>Get informally pre-screened before a formal application creates a record with a carrier. Different carriers weight the same health picture differently. A shop that knows the underwriting landscape can quietly match you to the company most likely to say yes. That single step meaningfully improves outcomes.</p>

<h2>The one thing not to do</h2>
<p>Do not wait for a birthday. LTC pricing does not step up cleanly on your birthday; it moves quarterly and annually with carrier reprices, and it moves with your health. If planning would help, plan now.</p>
'''

_HOW_MUCH_COST = '''
<p class="lede">Premiums for Long-Term Care Insurance vary widely, driven by five factors. This guide walks through each one and shows illustrative pricing examples so you can build a rough mental model before we talk numbers.</p>

<h2>The five factors that drive cost</h2>
<ol>
  <li><strong>Age at application.</strong> The single largest factor. Buying at 55 rather than 65 substantially reduces annual premium and gives inflation protection more time to work.</li>
  <li><strong>Health.</strong> Underwriting class matters. Preferred health typically saves 15% to 25% versus standard.</li>
  <li><strong>State.</strong> Some states have Partnership programs and additional consumer protections that affect pricing. State care-cost norms also drive design.</li>
  <li><strong>Benefit design.</strong> Monthly benefit, benefit period, elimination period, inflation protection, and shared care each move the number.</li>
  <li><strong>Policy type.</strong> Traditional standalone LTC, hybrid life/LTC, asset-based, and annuity+LTC each have their own economics.</li>
</ol>

<h2>Illustrative pricing examples</h2>
<p><strong>These are for education only.</strong> Real premiums depend on the actual applicant, state, carrier, and current rates. Do not use these as a quote.</p>

<div class="callout">
<p style="margin: 0;"><strong>Illustrative Example A: Traditional LTC. single female, age 55, preferred health.</strong></p>
<p style="margin: 8px 0 0;">$5,000 monthly benefit, 3-year benefit period, 90-day elimination period, 3% compound inflation. Annual premium in a common design range: roughly $2,400 to $3,600. This range varies significantly by state and carrier.</p>
</div>

<div class="callout">
<p style="margin: 0;"><strong>Illustrative Example B: Same design, same person, age 65.</strong></p>
<p style="margin: 8px 0 0;">Same monthly benefit, benefit period, elimination period, and inflation protection. Annual premium range roughly $4,500 to $6,800. The ten-year wait can effectively double the annual cost.</p>
</div>

<div class="callout">
<p style="margin: 0;"><strong>Illustrative Example C: Hybrid life/LTC. single male, age 60, preferred health.</strong></p>
<p style="margin: 8px 0 0;">Single-pay structure of roughly $100,000, or 10-pay structure of roughly $12,000 to $14,000 per year for ten years. Produces a death benefit and an LTC benefit pool that many families find easier to justify because someone always benefits from the funding.</p>
</div>

<div class="callout">
<p style="margin: 0;"><strong>Illustrative Example D: Asset-based LTC. married couple, both age 65, preferred health.</strong></p>
<p style="margin: 8px 0 0;">Single-premium structure repositioning existing savings, often $100,000 to $150,000 per person, that becomes a dedicated LTC pool with a death benefit if unused.</p>
</div>

<h2>What actually moves the number</h2>

<h3>The elimination period</h3>
<p>Going from a 30-day to a 90-day elimination period commonly reduces annual premium by 10% to 20%, in exchange for paying the first weeks of care yourself.</p>

<h3>Inflation protection</h3>
<p>3% compound inflation costs more than 5% simple. Choosing 3% compound over a fixed-benefit design commonly increases annual premium by 30% to 60%, and it is usually worth it because care costs rise faster than most fixed benefits keep up.</p>

<h3>The benefit period</h3>
<p>A 6-year benefit period may cost 40% more than a 3-year benefit period, but average claim durations vary widely. Many families choose the shorter design and buy back the difference with a higher monthly benefit.</p>

<h3>Shared care</h3>
<p>Adding a shared care rider on a joint policy increases premium modestly and can meaningfully change outcomes when one spouse&rsquo;s claim runs long.</p>

<h2>What to do with this</h2>
<p>Use these ranges to decide whether the conversation is worth having, then let a real quote reflect your actual age, state, health, and design. Numbers without those facts are guesses, and guesses in this space are usually misleading.</p>
'''

_TRADITIONAL_VS_HYBRID = '''
<p class="lede">There are three main ways to fund Long-Term Care Insurance today: traditional standalone LTC, hybrid life/LTC, and annuity-based strategies. Each has honest trade-offs. Here is how to think about which fits.</p>

<h2>Traditional standalone LTC</h2>
<p>The classic design. You pay an ongoing premium, and the policy pays a monthly benefit when triggers are met. The pool is dedicated entirely to long-term care.</p>

<h3>Where traditional works</h3>
<ul>
  <li>Healthy applicants in their 50s or early 60s can get the deepest LTC coverage per dollar with a traditional design.</li>
  <li>Comfortable with the possibility of a rate increase in exchange for the coverage efficiency.</li>
  <li>Value the largest possible care pool over other design considerations.</li>
</ul>
<h3>The honest trade-off</h3>
<p>Traditional LTC premiums are not contractually level. Carriers can request rate increases from state insurance regulators, and increases are possible over the life of the policy. If you never need care, no benefit is paid. Some families find both of those outcomes hard to accept.</p>

<h2>Hybrid life/LTC</h2>
<p>Permanent life insurance with a long-term care engine inside. If you need care, you can accelerate the death benefit to fund it. If you never need care, a death benefit remains for your heirs.</p>

<h3>Where hybrid works</h3>
<ul>
  <li>Applicants who dislike the &ldquo;use it or lose it&rdquo; profile of traditional coverage.</li>
  <li>Those who want contractually level premiums; many hybrid designs offer them.</li>
  <li>Households where either the LTC benefit or the death benefit would be genuinely useful.</li>
</ul>
<h3>The honest trade-off</h3>
<p>The dedicated LTC pool per dollar of premium is smaller than a traditional design. In exchange, someone always benefits, and premiums are typically contractually level.</p>

<h2>Asset-based LTC</h2>
<p>A single-premium or short-pay structure that repositions savings you were unlikely to spend, creating a dedicated LTC pool with a death benefit if unused.</p>

<h3>Where asset-based works</h3>
<ul>
  <li>Retirees with idle savings sitting in low-yielding accounts they will not touch.</li>
  <li>Those who prefer one payment and be done, rather than an ongoing premium schedule.</li>
  <li>Applicants who like the efficiency of leveraging a lump sum into a substantially larger care pool.</li>
</ul>
<h3>The honest trade-off</h3>
<p>The single-payment commitment is real, and access to the underlying account value is typically limited during a surrender schedule. The design fits money you were not planning to spend anyway.</p>

<h2>Annuity + LTC features</h2>
<p>Some annuities include income doublers or LTC riders that increase payouts or provide leverage if long-term care is later needed. Simplified underwriting is common.</p>

<h3>Where annuity-based works</h3>
<ul>
  <li>Applicants whose health rules out traditional or hybrid coverage.</li>
  <li>Those who want retirement income first, with LTC leverage as a secondary benefit.</li>
</ul>
<h3>The honest trade-off</h3>
<p>The leverage does not match dedicated LTC coverage. When health limits options, though, an annuity-based LTC strategy is often the honest answer, and a funded plan beats an unfunded intention.</p>

<h2>A quick side-by-side</h2>
<p><strong>Deepest care pool per dollar for a healthy applicant:</strong> traditional LTC.<br />
<strong>&ldquo;Someone always benefits&rdquo; and level premiums:</strong> hybrid life/LTC.<br />
<strong>Single-payment structure repositioning idle savings:</strong> asset-based LTC.<br />
<strong>Simplified underwriting when other options are closed:</strong> annuity with LTC features.</p>

<h2>How we choose</h2>
<p>Age, health, cash flow preference, and how you feel about paying premiums for a benefit you may or may not use. There is no universally right answer. The right answer for you emerges from a working session that looks honestly at your situation and compares real quotes from the carriers likely to say yes.</p>
'''

THUMBS = {
    "what-long-term-care-insurance-covers": "ltc-covers-thumb.jpg",
    "medicare-vs-long-term-care-insurance": "medicare-vs-ltc-thumb.jpg",
    "when-should-you-buy-long-term-care-insurance": "when-to-buy-thumb.jpg",
    "how-much-does-long-term-care-insurance-cost": "cost-thumb.jpg",
    "traditional-vs-hybrid-long-term-care-insurance": "traditional-vs-hybrid-thumb.jpg",
}

POSTS = [
    ("what-long-term-care-insurance-covers",
     "What Long-Term Care Insurance actually covers",
     "Long-Term Care", "June 2026", 6,
     "Adult daughter and mother reviewing paperwork calmly at a kitchen table",
     _WHAT_LTC_COVERS, "ltc"),
    ("medicare-vs-long-term-care-insurance",
     "Medicare vs. Long-Term Care Insurance: what each one actually does",
     "Long-Term Care", "June 2026", 5,
     "Senior man at a desk reading Medicare enrollment information",
     _MEDICARE_VS_LTC, "ltc"),
    ("when-should-you-buy-long-term-care-insurance",
     "When should you buy Long-Term Care Insurance?",
     "Long-Term Care", "June 2026", 7,
     "Couple in their fifties walking a tree-lined path in autumn",
     _WHEN_TO_BUY, "ltc"),
    ("how-much-does-long-term-care-insurance-cost",
     "How much does Long-Term Care Insurance cost?",
     "Long-Term Care", "June 2026", 8,
     "Woman at a kitchen island reviewing a household budget",
     _HOW_MUCH_COST, "general"),
    ("traditional-vs-hybrid-long-term-care-insurance",
     "Traditional vs. hybrid vs. annuity-based Long-Term Care planning",
     "Long-Term Care", "June 2026", 7,
     "Couple reviewing a policy document with an advisor over video call",
     _TRADITIONAL_VS_HYBRID, "ltc"),
]
