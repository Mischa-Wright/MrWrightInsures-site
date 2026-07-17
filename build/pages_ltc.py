"""Long-Term Care flagship page and Start Here chooser."""

def build(render, img_slot, CAL, GR, RAMSEY):
    _ltc(render, img_slot, CAL, GR)
    _start(render, img_slot, CAL, GR)


def _ltc(render, img_slot, CAL, GR):
    body = f'''
<section class="hero" style="padding-bottom: 48px;">
  <div class="wrap">
    <div class="hero-grid">
      <div>
        <span class="eyebrow">Long-Term Care Insurance</span>
        <h1>Plan for care while you still have every option.</h1>
        <p class="lede">Long-Term Care Insurance funds the ongoing help most families eventually need, and Medicare does not cover. The choice about how, where, and who provides that care stays with you when a plan is in place.</p>
        <div class="btn-row">
          <a class="btn btn-primary btn-lg" href="{CAL["ltc"]}" target="_blank" rel="noopener">Book an LTC Intro Call <span class="arrow" aria-hidden="true">→</span></a>
        </div>
      </div>
      <div class="hero-media">
        {img_slot("images/generated/ltc-hero.jpg", "Multigenerational family talking together in a sunlit living room")}
      </div>
    </div>
  </div>
</section>

<section class="alt tight">
  <div class="wrap-mid">
    <span class="eyebrow">Section navigation</span>
    <div class="btn-row" style="margin-top:12px; gap: 6px;">
      <a class="btn btn-ghost btn-sm" href="#what-it-covers">What it covers</a>
      <a class="btn btn-ghost btn-sm" href="#medicare-vs-ltc">Medicare vs. LTC</a>
      <a class="btn btn-ghost btn-sm" href="#policy-types">Policy types</a>
      <a class="btn btn-ghost btn-sm" href="#policy-design">Policy design</a>
      <a class="btn btn-ghost btn-sm" href="#underwriting">Underwriting</a>
      <a class="btn btn-ghost btn-sm" href="#process">Our process</a>
      <a class="btn btn-ghost btn-sm" href="#faq">FAQ</a>
    </div>
  </div>
</section>

<section id="what-it-covers">
  <div class="wrap-mid">
    <h2>What Long-Term Care Insurance helps pay for</h2>
    <p class="lede">Modern policies fund care wherever you receive it, not just in a nursing home. Benefits are paid when you cannot perform a set number of activities of daily living or need supervision because of cognitive decline.</p>

    <div class="definitions mt-2">
      <div class="definition">
        <h4>Care at home</h4>
        <p>Home care aides, home health services, and in some contracts modest help with home modifications so care can be delivered where you live.</p>
      </div>
      <div class="definition">
        <h4>Assisted living</h4>
        <p>Monthly benefits toward residence in an assisted living community when help with daily activities is needed but full nursing care is not.</p>
      </div>
      <div class="definition">
        <h4>Memory care</h4>
        <p>Specialized cognitive care communities. This is where LTC coverage often matters most, because Medicare covers essentially none of this care.</p>
      </div>
      <div class="definition">
        <h4>Skilled nursing</h4>
        <p>Long stays in a skilled nursing facility, once short-term Medicare coverage ends and the care becomes custodial rather than rehabilitative.</p>
      </div>
      <div class="definition">
        <h4>Adult day services</h4>
        <p>Structured daytime care that lets a working family caregiver keep their job and gives the person receiving care social connection.</p>
      </div>
      <div class="definition">
        <h4>Care coordination</h4>
        <p>Many contracts include a care coordinator who helps a family navigate providers and paperwork at the moment they most need it.</p>
      </div>
    </div>
  </div>
</section>

<section id="medicare-vs-ltc" class="alt">
  <div class="wrap-mid">
    <span class="eyebrow">Common misunderstanding</span>
    <h2>Medicare and Long-Term Care Insurance do different jobs.</h2>
    <p class="lede">This confusion causes real financial damage every year. Here is the clean split.</p>

    <div class="compare">
      <div class="head">
        <h3 style="color:inherit; margin-bottom: 8px;">Medicare</h3>
        <ul>
          <li>Hospital and doctor coverage</li>
          <li>Short-term skilled care after a qualifying hospital stay (up to 100 days, most fully paid only during days 1&ndash;20)</li>
          <li>Limited home health for medically necessary skilled care</li>
          <li>Hospice</li>
        </ul>
      </div>
      <div class="head rust">
        <h3 style="color:inherit; margin-bottom: 8px;">Long-Term Care Insurance</h3>
        <ul>
          <li>Ongoing custodial care (help with bathing, dressing, eating, transferring)</li>
          <li>Cognitive supervision for dementia</li>
          <li>Care at home, in assisted living, in memory care, or in skilled nursing</li>
          <li>Care coordination and, in many contracts, family caregiver support</li>
        </ul>
      </div>
      <div>
        <p style="margin:0; color: var(--ink-2); font-size: 0.94rem;">Medicare is not a long-term-care program. It was never designed to fund the years-long custodial care many families end up needing.</p>
      </div>
      <div>
        <p style="margin:0; color: var(--ink-2); font-size: 0.94rem;">Certain policies also include partial benefits during a rehabilitation phase, letting a family bring in extra help before the Medicare stay ends.</p>
      </div>
    </div>
  </div>
</section>

<section id="policy-types">
  <div class="wrap-mid">
    <span class="eyebrow">Ways to fund the plan</span>
    <h2>There is more than one way to build long-term care into a plan.</h2>
    <p class="lede">Which design fits depends on your health, age, cash flow, and how you feel about paying premiums for a benefit you may or may not use.</p>

    <div class="compare mt-2">
      <div class="head"><h3 style="color:inherit; margin-bottom:8px;">Traditional LTC</h3><ul><li>Level or level-to-a-point premiums</li><li>Deepest care coverage per dollar for healthy applicants</li><li>Rate increases are possible over time and require regulatory approval</li></ul></div>
      <div class="head rust"><h3 style="color:inherit; margin-bottom:8px;">Hybrid life / LTC</h3><ul><li>Life insurance with a long-term care engine inside it</li><li>If you never need care, a death benefit remains</li><li>Many designs offer contractually level premiums</li></ul></div>
      <div>
        <h3 style="font-size:1.05rem; margin-bottom:8px;">Asset-based LTC</h3>
        <p style="margin:0; color: var(--ink-2); font-size:0.94rem;">A single or short-pay premium repositions savings you were unlikely to spend, creating a dedicated LTC pool with a death benefit if unused.</p>
      </div>
      <div>
        <h3 style="font-size:1.05rem; margin-bottom:8px;">Annuity + LTC features</h3>
        <p style="margin:0; color: var(--ink-2); font-size:0.94rem;">Some annuities include income doublers or LTC riders. Often useful when health makes traditional or hybrid coverage unavailable. Simplified underwriting typical.</p>
      </div>
    </div>

    <p style="margin-top: var(--sp-5); color: var(--ink-2); font-size:0.94rem;">Partnership-qualified policies, available in most states, provide additional Medicaid asset protection if benefits are ever exhausted. Availability and terms vary by state.</p>
  </div>
</section>

<section id="policy-design" class="alt">
  <div class="wrap-mid">
    <span class="eyebrow">Policy design</span>
    <h2>The four dials that shape both the coverage and the premium.</h2>

    <div class="definitions mt-2">
      <div class="definition"><h4>Monthly benefit</h4><p>The maximum a policy pays each month. Chosen relative to current care costs in your area and how much of the bill you want the policy to cover.</p></div>
      <div class="definition"><h4>Benefit period</h4><p>How long benefits are payable. Commonly 2 to 6 years. Some pools work as a total dollar amount rather than a strict number of years.</p></div>
      <div class="definition"><h4>Elimination period</h4><p>A deductible measured in days rather than dollars. A longer elimination period lowers the premium in exchange for paying the first weeks of care yourself.</p></div>
      <div class="definition"><h4>Inflation protection</h4><p>Care costs rise. Inflation options grow the monthly benefit over time so a policy purchased today still pays a meaningful share of care 20 years from now.</p></div>
      <div class="definition"><h4>Shared care</h4><p>Available on many joint policies. Lets spouses draw from each other&rsquo;s benefit pool if one person&rsquo;s claim runs long.</p></div>
      <div class="definition"><h4>Underwriting</h4><p>LTC coverage is medically underwritten. Applying while healthy is the single largest factor in what is available to you and at what price.</p></div>
    </div>

    <h3 style="margin-top: 64px;">Elimination period at a glance</h3>
    <div class="timeline" role="img" aria-label="Timeline showing the elimination period across four phases">
      <div class="phase">
        <h4>Day 0</h4>
        <span class="day">Care begins</span>
        <p>You start receiving qualifying care after triggering the policy&rsquo;s benefit conditions.</p>
      </div>
      <div class="phase">
        <h4>Days 1&ndash;90 (typical)</h4>
        <span class="day">Elimination period</span>
        <p>You cover care during this deductible-like window. Choosing longer reduces premium.</p>
      </div>
      <div class="phase active">
        <h4>Day 91+</h4>
        <span class="day">Benefits begin</span>
        <p>Policy monthly benefits begin paying up to the contract maximum, based on qualifying expenses.</p>
      </div>
      <div class="phase">
        <h4>Ongoing</h4>
        <span class="day">Through benefit period</span>
        <p>Benefits continue until the pool is exhausted or you no longer meet the benefit conditions.</p>
      </div>
    </div>
  </div>
</section>

<section id="underwriting">
  <div class="wrap-mid">
    <div class="grid-2 narrow-side">
      <div>
        <span class="eyebrow">Underwriting reality</span>
        <h2>Health today is the gate to coverage tomorrow.</h2>
        <p>Long-Term Care Insurance is medically underwritten. Underwriters are not asking whether you might get sick, they are asking how likely you are to need extended help with daily living.</p>
        <p>Well-managed conditions are routinely insurable. Memory or cognitive concerns are the most sensitive area, and a dementia diagnosis generally makes traditional coverage unavailable. Carriers genuinely differ, which is where an independent shop with LTC experience earns its keep.</p>
        <p>If traditional approval is unlikely, we look at hybrid designs and annuity-based strategies with simplified or no underwriting. There is almost always a next-best plan.</p>
      </div>
      <div>
        <div class="reviews-band" style="grid-template-columns: 1fr; text-align: left; background: var(--cream-light);">
          <div>
            <h3 style="font-size:1.1rem;">A note on informal pre-screening</h3>
            <p style="color: var(--ink-2); font-size:0.94rem;">Before a formal application creates a record with a carrier, we walk through your health picture informally and match it to the company most likely to say yes. That single step meaningfully improves outcomes.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section id="process" class="alt">
  <div class="wrap-mid">
    <span class="eyebrow">How we work</span>
    <h2>The consultation, step by step.</h2>
    <ol class="steps grid-3 mt-2">
      <li class="step">
        <h3>Short intro call</h3>
        <p>Fifteen minutes to understand what prompted your call and confirm this is a fit.</p>
      </li>
      <li class="step">
        <h3>Working session</h3>
        <p>Longer conversation. Age, health, state, existing coverage, and what you are protecting.</p>
      </li>
      <li class="step">
        <h3>Side-by-side options</h3>
        <p>Real quotes from appropriate carriers with the trade-offs stated honestly.</p>
      </li>
    </ol>
  </div>
</section>

<section id="faq">
  <div class="wrap-mid">
    <div class="center mb-2">
      <span class="eyebrow">Frequently asked</span>
      <h2>Questions clients ask us most.</h2>
    </div>
    <div class="faq">
      <details>
        <summary>What triggers benefits?</summary>
        <div class="answer"><p>In most contracts, benefits become payable when you cannot perform two of six activities of daily living (bathing, dressing, eating, transferring, toileting, continence) expected to last at least 90 days, or you need substantial supervision because of cognitive impairment. A licensed provider or care coordinator documents the trigger.</p></div>
      </details>
      <details>
        <summary>Can premiums increase on a traditional LTC policy?</summary>
        <div class="answer"><p>Yes. Traditional LTC premiums are not guaranteed level. Carriers can request rate increases from state insurance regulators, and increases are possible over the life of the policy. Hybrid life/LTC and asset-based designs often offer contractually level premiums, one reason many families now prefer them.</p></div>
      </details>
      <details>
        <summary>Is there tax-advantaged treatment?</summary>
        <div class="answer"><p>Certain LTC policies (qualified plans) offer favorable tax treatment on benefits and, in some cases, premiums. Business-owner premium deductibility rules are more generous but limited by age. Tax treatment depends on your situation; consult your tax advisor.</p></div>
      </details>
      <details>
        <summary>What is a Partnership-qualified policy?</summary>
        <div class="answer"><p>A Partnership-qualified policy provides additional Medicaid asset protection if benefits are ever exhausted, based on the amount the policy paid out. Availability, benefit amounts, and rules vary by state.</p></div>
      </details>
      <details>
        <summary>How is a claim actually filed?</summary>
        <div class="answer"><p>Care needs are documented by a licensed practitioner. The carrier reviews the claim, and once the elimination period is satisfied, monthly benefits are paid according to the contract. Many policies include care coordinator services to help a family through the process at exactly the moment it is most overwhelming.</p></div>
      </details>
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="wrap-mid">
    <h2>Talk it through with a specialist.</h2>
    <p>A short LTC-focused conversation. No sales pitch, no obligation, and a real answer either way about whether this fits your situation.</p>
    <a class="btn btn-invert btn-lg" href="{CAL["ltc"]}" target="_blank" rel="noopener">Book an LTC Intro Call <span class="arrow" aria-hidden="true">→</span></a>
  </div>
</section>
'''
    render(
        path="long-term-care-insurance.html",
        title="Long-Term Care Insurance | Mischa Wright Insurance Agency",
        description="Independent Long-Term Care Insurance guidance: coverage explained, Medicare vs. LTC, policy types, benefit design, underwriting, and the consultation process. CLTC advisor, licensed team nationwide.",
        body=body,
        active="ltc",
        depth=0,
    )


def _start(render, img_slot, CAL, GR):
    body = f'''
<section class="hero" style="padding-bottom: 32px;">
  <div class="wrap-mid center">
    <span class="eyebrow">Start Here</span>
    <h1>What would you like help with?</h1>
    <p class="lede" style="margin: 0 auto 40px; max-width: 60ch;">Choose the type of insurance guidance you are looking for. We will take you straight to the right next step so you do not have to fill out anything twice.</p>
  </div>
</section>

<section style="padding-top: 0;">
  <div class="wrap-mid">
    <div class="chooser">
      <div class="chooser-grid">
        <a class="chooser-card primary" href="long-term-care-insurance.html?service=ltc" data-service="ltc">
          <span class="lbl">Our flagship specialty</span>
          <h3>Long-Term Care Insurance</h3>
          <p>Home care, assisted living, memory care, and skilled nursing coverage. Traditional, hybrid, and asset-based designs. Best-fit carrier matching.</p>
          <div style="margin-top:12px"><span style="font-size:0.92rem; opacity:0.9;">Continue to Long-Term Care →</span></div>
        </a>

        <a class="chooser-card" href="annuities.html?service=annuities" data-service="annuities">
          <span class="lbl">Retirement income</span>
          <h3>Annuities</h3>
          <p>Income planning, principal-protection strategies, and riders that include LTC features.</p>
        </a>

        <a class="chooser-card" href="life-insurance.html?service=life" data-service="life">
          <span class="lbl">Family protection</span>
          <h3>Life Insurance</h3>
          <p>Term, permanent, and hybrid life/LTC designs matched to the actual job.</p>
        </a>

        <a class="chooser-card" href="medicare.html?service=medicare" data-service="medicare">
          <span class="lbl">Referral service</span>
          <h3>Medicare</h3>
          <p>Our licensed team can help connect you with appropriate Medicare guidance.</p>
        </a>

        <a class="chooser-card" href="disability-insurance.html?service=disability" data-service="disability">
          <span class="lbl">Income protection</span>
          <h3>Disability Insurance</h3>
          <p>Individual coverage for professionals and business owners. Own-occupation definitions, BOE, buy-sell funding.</p>
        </a>

        <a class="chooser-card" href="contact.html?service=general" data-service="general">
          <span class="lbl">Not sure yet</span>
          <h3>I do not know where to start</h3>
          <p>Send a short message and we will help you figure out where to begin.</p>
        </a>
      </div>
    </div>

    <div class="center mt-3">
      <p style="color: var(--ink-2); font-size: 0.94rem;">Prefer to talk first? <a href="{CAL["general"]}" target="_blank" rel="noopener">Book a 15-minute call</a> or call us at <a href="tel:8583459952">858-345-9952</a>.</p>
    </div>
  </div>
</section>
'''
    render(
        path="start.html",
        title="Start Here | Mischa Wright Insurance Agency",
        description="Choose the type of insurance guidance you are looking for and we will take you to the right next step. Long-Term Care, annuities, life insurance, Medicare referrals, or disability coverage.",
        body=body,
        active="",
        depth=0,
    )
