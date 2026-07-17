"""Annuities, Life, Medicare (referral), Disability (form-based) pages."""

def build(render, img_slot, CAL, GR, RAMSEY):
    _annuities(render, img_slot, CAL)
    _life(render, img_slot, CAL)
    _medicare(render, img_slot, CAL)
    _disability(render, img_slot, CAL)


def _annuities(render, img_slot, CAL):
    body = f'''
<section class="hero">
  <div class="wrap">
    <div class="hero-grid">
      <div>
        <span class="eyebrow">Annuities</span>
        <h1>Turning savings into income that can outlast retirement.</h1>
        <p class="lede">Annuities are insurance contracts, not investments. Used carefully, they can add contractual income guarantees, protect principal from market loss, or reposition savings toward future long-term care needs.</p>
        <a class="btn btn-primary btn-lg" href="{CAL["annuity"]}" target="_blank" rel="noopener">Book an Annuity Call <span class="arrow" aria-hidden="true">→</span></a>
      </div>
      <div class="hero-media">
        {img_slot("images/generated/annuities-hero.jpg", "Retired couple walking along a tree-lined path in morning light")}
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap-mid">
    <h2>The three main jobs an annuity can do.</h2>
    <div class="definitions mt-2">
      <div class="definition">
        <h4>Fixed annuities</h4>
        <p>A declared interest rate for a set period. Conceptually similar to a CD, with tax deferral. Access is limited during the surrender schedule.</p>
      </div>
      <div class="definition">
        <h4>Fixed indexed annuities</h4>
        <p>Interest linked to a market index&rsquo;s performance, with a contractual floor that protects principal from market loss. Growth is moderated by caps or participation rates. This is not direct market investment.</p>
      </div>
      <div class="definition">
        <h4>Income annuities and income riders</h4>
        <p>Convert savings into a guaranteed paycheck for a set period or for life. Some riders include enhanced payouts if long-term care is later needed.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap-mid">
    <div class="grid-2 narrow-side">
      <div>
        <span class="eyebrow">Where annuities fit LTC planning</span>
        <h2>An underused answer when health has closed other doors.</h2>
        <p>When traditional or hybrid LTC coverage is unavailable due to health, an annuity-based strategy is often still open. Some annuities include income doublers that increase payouts if you cannot perform certain activities of daily living. Others include LTC riders that multiply the account value for qualifying care expenses.</p>
        <p>Underwriting is typically simplified or none at all. The leverage does not match dedicated LTC insurance, but a funded plan beats an unfunded intention.</p>
      </div>
      <div>
        <div class="callout" style="background: var(--cream-light); border-left: 3px solid var(--rust); padding: 24px; border-radius: 0 8px 8px 0;">
          <h3 style="font-size:1.1rem; margin-bottom: 10px;">Honest trade-offs</h3>
          <ul style="padding-left: 1.2em; color: var(--ink-2); font-size:0.95rem; margin:0;">
            <li>Surrender schedules limit access to principal early in the contract</li>
            <li>Withdrawals above contract limits may reduce future income and account values</li>
            <li>Rider charges reduce interest credits</li>
            <li>Tax treatment depends on your situation; consult your tax advisor</li>
            <li>Certain annuities can provide contractual guarantees, subject to the claims-paying ability of the issuing insurance company</li>
            <li>Annuities are not right for everyone</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap-mid">
    <span class="eyebrow">How we approach it</span>
    <h2>Suitability first, product second.</h2>
    <p class="lede">We start with your income needs, timeline, and existing resources. Then we compare options from multiple highly rated insurance companies and explain the surrender periods, rider charges, and income mechanics before anything is signed.</p>
  </div>
</section>

<section class="cta-band">
  <div class="wrap-mid">
    <h2>Is a guaranteed income tool the right fit?</h2>
    <p>A short conversation is the honest way to find out. We will look at whether annuity strategies belong in your plan, and where they do not.</p>
    <a class="btn btn-invert btn-lg" href="{CAL["annuity"]}" target="_blank" rel="noopener">Book an Annuity Call <span class="arrow" aria-hidden="true">→</span></a>
  </div>
</section>
'''
    render(
        path="annuities.html",
        title="Annuities | Retirement Income Planning | Mischa Wright Insurance Agency",
        description="Independent guidance on fixed, fixed indexed, and income annuities. Suitability-first, education-first. LTC-linked income features where they fit. Licensed team nationwide.",
        body=body, active="", depth=0,
    )


def _life(render, img_slot, CAL):
    body = f'''
<section class="hero">
  <div class="wrap">
    <div class="hero-grid">
      <div>
        <span class="eyebrow">Life Insurance</span>
        <h1>Cover the jobs the money has to do.</h1>
        <p class="lede">Term, permanent, and hybrid life/LTC designs. Choose the structure by what the coverage needs to do, not the other way around.</p>
        <a class="btn btn-primary btn-lg" href="{CAL["life"]}" target="_blank" rel="noopener">Request a Life Insurance Quote <span class="arrow" aria-hidden="true">→</span></a>
        <p class="supporting">To give you useful numbers rather than generic estimates, we start with a short conversation about age, state, and health.</p>
      </div>
      <div class="hero-media">
        {img_slot("images/generated/life-hero.jpg", "Parents in a bright living room playing with two young children")}
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap-mid">
    <span class="eyebrow">Getting the structure right</span>
    <h2>Term for temporary jobs, permanent where lifetime coverage earns its cost.</h2>

    <div class="definitions mt-2">
      <div class="definition">
        <h4>Term insurance</h4>
        <p>Level premium for a set period (commonly 10, 20, or 30 years). Efficient for time-limited needs: the mortgage, income replacement while children are dependent, business obligations.</p>
      </div>
      <div class="definition">
        <h4>Permanent insurance</h4>
        <p>Lifetime coverage with cash value accumulation. Fits legacy planning, estate liquidity, and situations where lifetime death benefit or cash-value flexibility matters.</p>
      </div>
      <div class="definition">
        <h4>Hybrid life / LTC</h4>
        <p>Permanent life insurance with a long-term care engine inside. If you never need care, a death benefit remains. Increasingly common because someone always benefits from the funding.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap-mid">
    <h2>How much coverage is enough?</h2>
    <p>Rules of thumb (ten times income is the classic) are starting points, not answers. The better method is to add up the actual jobs the money must do: pay off the mortgage, replace income for a chosen number of years, fund education, cover final expenses. For many families the honest number is larger than they guessed and less expensive to insure than they feared.</p>
    <h3 style="margin-top: 40px;">What drives the price</h3>
    <p>Age, health, tobacco use, coverage amount, term length, and carrier appetite. Like every underwritten coverage, life insurance is best priced when you are young and healthy, which is why we start with a health-honest conversation before running numbers.</p>
  </div>
</section>

<section class="cta-band">
  <div class="wrap-mid">
    <h2>See what actual numbers look like for your situation.</h2>
    <p>Short conversation, side-by-side comparisons from multiple highly rated carriers, and a design that matches what the coverage actually needs to accomplish.</p>
    <a class="btn btn-invert btn-lg" href="{CAL["life"]}" target="_blank" rel="noopener">Request a Life Insurance Quote <span class="arrow" aria-hidden="true">→</span></a>
  </div>
</section>
'''
    render(
        path="life-insurance.html",
        title="Life Insurance | Term, Permanent, and Hybrid Designs | Mischa Wright Insurance Agency",
        description="Independent life insurance guidance: term, permanent, and hybrid life/LTC. Independent underwriting comparison across multiple highly rated carriers.",
        body=body, active="", depth=0,
    )


def _medicare(render, img_slot, CAL):
    # Medicare is referral. Form-based, no Calendly.
    body = f'''
<section class="hero" style="padding-bottom: 48px;">
  <div class="wrap">
    <div class="hero-grid">
      <div>
        <span class="eyebrow">Medicare</span>
        <h1>Talk to a Medicare specialist on our licensed team.</h1>
        <p class="lede">Medicare choices are personal. Our licensed team can help connect you with appropriate guidance on Supplement, Advantage, and prescription drug coverage.</p>
      </div>
      <div class="hero-media">
        {img_slot("images/generated/medicare-hero.jpg", "Senior woman at a tidy desk reading Medicare enrollment information with reading glasses")}
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap-mid">
    <div class="grid-2 wide-side">
      <div>
        <span class="eyebrow">What we help with</span>
        <h2>Coverage choices, plan reviews, and the enrollment windows that matter.</h2>
        <ul style="padding-left: 1.2em; line-height: 1.8; color: var(--ink);">
          <li>Medicare Supplement (Medigap) options</li>
          <li>Medicare Advantage plan choices in your area</li>
          <li>Part D prescription drug coverage</li>
          <li>Initial enrollment, open enrollment, and special enrollment period timing</li>
          <li>Annual plan review as your health and prescriptions change</li>
          <li>How Medicare fits alongside employer or retiree coverage</li>
        </ul>
        <p style="color: var(--ink-2); margin-top: 24px; font-size: 0.94rem;">Plan availability varies by county and carrier. We are not affiliated with Medicare or any government agency.</p>
      </div>
      <div>
        <form class="form" data-lead-form aria-label="Medicare help request">
          <h3 style="font-family: var(--serif); font-size: 1.35rem; margin-bottom: 20px;">Request Medicare help</h3>
          <input type="hidden" name="product_interest" value="Medicare" data-preset="Medicare" />
          <input type="hidden" name="source_page" value="/medicare" />
          <input type="hidden" name="referrer" value="" />
          <input type="hidden" name="utm_source" value="" />
          <input type="hidden" name="utm_medium" value="" />
          <input type="hidden" name="utm_campaign" value="" />

          <div class="row">
            <div class="field"><label for="med_first">First name</label><input id="med_first" name="first_name" type="text" required autocomplete="given-name" /><span class="err-msg">Required</span></div>
            <div class="field"><label for="med_last">Last name</label><input id="med_last" name="last_name" type="text" required autocomplete="family-name" /><span class="err-msg">Required</span></div>
          </div>
          <div class="row">
            <div class="field"><label for="med_email">Email</label><input id="med_email" name="email" type="email" required autocomplete="email" /><span class="err-msg">A valid email is required</span></div>
            <div class="field"><label for="med_phone">Phone</label><input id="med_phone" name="phone" type="tel" required autocomplete="tel" placeholder="(555) 555-1234" /><span class="err-msg">A valid US phone number is required</span></div>
          </div>
          <div class="field">
            <label for="med_state">State</label>
            <select id="med_state" name="state" required>
              <option value="">Select your state</option>
              {_state_options()}
            </select>
            <span class="err-msg">Required</span>
          </div>
          <div class="field">
            <label for="med_contact">Preferred contact method</label>
            <select id="med_contact" name="contact_method" required>
              <option value="">Choose one</option>
              <option>Phone</option><option>Email</option><option>Text</option>
            </select>
            <span class="err-msg">Required</span>
          </div>
          <div class="field">
            <label for="med_msg">Anything we should know?</label>
            <textarea id="med_msg" name="message" placeholder="Coverage question, upcoming enrollment date, current plan situation..."></textarea>
            <span class="hint sensitive-warning">Please do not include Social Security numbers, financial account information, medical records, or other sensitive personal information.</span>
          </div>
          <div class="checkbox">
            <input id="med_consent" name="consent" type="checkbox" required />
            <label for="med_consent">I agree to be contacted by Mischa Wright Insurance Agency about my request. Message and data rates may apply.</label>
          </div>
          <div class="form-status" role="status" aria-live="polite"></div>
          <button type="submit" class="btn btn-primary" data-label="Request Medicare Help">Request Medicare Help <span class="arrow" aria-hidden="true">→</span></button>
        </form>
      </div>
    </div>
  </div>
</section>
'''
    render(
        path="medicare.html",
        title="Medicare Help | Supplement, Advantage, Part D | Mischa Wright Insurance Agency",
        description="Request Medicare guidance from our licensed team. Supplement, Advantage, and Part D options. We are not affiliated with Medicare or any government agency; plan availability varies by county and carrier.",
        body=body, active="", depth=0,
    )


def _disability(render, img_slot, CAL):
    body = f'''
<section class="hero">
  <div class="wrap">
    <div class="hero-grid">
      <div>
        <span class="eyebrow">Disability Insurance</span>
        <h1>Your income is the asset behind every other plan.</h1>
        <p class="lede">A working professional&rsquo;s future income is often larger than their home, retirement account, and life insurance combined. Disability insurance protects it.</p>
        <a class="btn btn-primary btn-lg" href="#quote-form">Request a Disability Insurance Quote <span class="arrow" aria-hidden="true">↓</span></a>
      </div>
      <div class="hero-media">
        {img_slot("images/generated/disability-hero.jpg", "Professional working at a bright home studio desk")}
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap-mid">
    <span class="eyebrow">What it does</span>
    <h2>Replace a portion of your income when illness or injury stops you from working.</h2>
    <p>Long-term disability coverage typically replaces up to about 60% of income and can pay for years, often to age 65 or 67. Benefits from a policy you pay for personally with after-tax dollars are generally received income-tax-free for federal purposes; tax treatment depends on your situation and consulting your tax advisor is appropriate.</p>
  </div>
</section>

<section>
  <div class="wrap-mid">
    <h2>The provisions that decide whether coverage actually pays.</h2>
    <p class="lede">The words in a policy matter more than the price. Two policies at the same premium can behave very differently at claim time.</p>

    <div class="definitions mt-2">
      <div class="definition">
        <h4>Own-occupation definition</h4>
        <p>Pays if you cannot perform your specific profession, even if you could do other work. Critical for specialized professionals.</p>
      </div>
      <div class="definition">
        <h4>Any-occupation definition</h4>
        <p>Pays only if you cannot do essentially any work. Common in group coverage; a much narrower protection.</p>
      </div>
      <div class="definition">
        <h4>Residual / partial disability</h4>
        <p>Pays proportional benefits when you can work part-time or in a reduced capacity because of the condition.</p>
      </div>
      <div class="definition">
        <h4>Non-cancelable</h4>
        <p>The carrier cannot cancel or increase premiums as long as premiums are paid.</p>
      </div>
      <div class="definition">
        <h4>Guaranteed renewable</h4>
        <p>The policy stays in force but premiums may change by class. A weaker guarantee than non-cancelable.</p>
      </div>
      <div class="definition">
        <h4>Elimination period</h4>
        <p>Waiting period before benefits start, commonly 90 or 180 days. Longer elimination periods reduce premium if you have adequate emergency reserves.</p>
      </div>
      <div class="definition">
        <h4>Benefit period</h4>
        <p>How long benefits are payable if the disability continues. Long-term policies commonly run to age 65 or 67.</p>
      </div>
      <div class="definition">
        <h4>Benefit amount</h4>
        <p>The monthly benefit is set relative to income, typically 60% to 66&frac23;% of covered earnings, subject to carrier issue limits.</p>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap-mid">
    <h2>Business owner considerations.</h2>
    <div class="definitions mt-2">
      <div class="definition"><h4>Business Overhead Expense (BOE)</h4><p>Covers ongoing business expenses (rent, payroll, utilities) if you are disabled and can no longer generate revenue.</p></div>
      <div class="definition"><h4>Disability buy-sell funding</h4><p>Provides the funds a partner or buy-sell agreement needs to purchase a disabled owner&rsquo;s interest at a defined point.</p></div>
      <div class="definition"><h4>Key person</h4><p>Coverage on individuals whose disability would materially impact the business. Often paired with a written continuity plan.</p></div>
    </div>
  </div>
</section>

<section id="quote-form">
  <div class="wrap-mid">
    <div class="grid-2 narrow-side">
      <div>
        <span class="eyebrow">Get useful numbers</span>
        <h2>Request a disability insurance quote.</h2>
        <p>Because occupation classification, income documentation, and health history drive the design, real disability quotes begin with a short conversation. Send the form and we will reach out to schedule.</p>
        <h3 style="margin-top: 32px; font-size: 1.05rem;">Common employer-coverage gaps</h3>
        <ul style="color: var(--ink-2); font-size: 0.94rem;">
          <li>Benefits end if you leave the job</li>
          <li>Employer-paid benefits are typically taxable</li>
          <li>Coverage often uses an any-occupation definition after the first two years</li>
          <li>Bonus, commission, and equity income are often not covered</li>
        </ul>
      </div>
      <div>
        <form class="form" data-lead-form aria-label="Disability insurance quote request">
          <input type="hidden" name="product_interest" value="Disability Insurance" data-preset="Disability Insurance" />
          <input type="hidden" name="source_page" value="/disability-insurance" />
          <input type="hidden" name="referrer" value="" />
          <input type="hidden" name="utm_source" value="" />
          <input type="hidden" name="utm_medium" value="" />
          <input type="hidden" name="utm_campaign" value="" />

          <div class="row">
            <div class="field"><label for="di_first">First name</label><input id="di_first" name="first_name" type="text" required /><span class="err-msg">Required</span></div>
            <div class="field"><label for="di_last">Last name</label><input id="di_last" name="last_name" type="text" required /><span class="err-msg">Required</span></div>
          </div>
          <div class="row">
            <div class="field"><label for="di_email">Email</label><input id="di_email" name="email" type="email" required /><span class="err-msg">A valid email is required</span></div>
            <div class="field"><label for="di_phone">Phone</label><input id="di_phone" name="phone" type="tel" required /><span class="err-msg">A valid US phone number is required</span></div>
          </div>
          <div class="field">
            <label for="di_state">State</label>
            <select id="di_state" name="state" required>
              <option value="">Select your state</option>
              {_state_options()}
            </select>
            <span class="err-msg">Required</span>
          </div>
          <div class="field">
            <label for="di_contact">Preferred contact method</label>
            <select id="di_contact" name="contact_method" required>
              <option value="">Choose one</option>
              <option>Phone</option><option>Email</option><option>Text</option>
            </select>
            <span class="err-msg">Required</span>
          </div>
          <div class="field">
            <label for="di_msg">Occupation and anything else useful</label>
            <textarea id="di_msg" name="message" placeholder="Occupation, employer coverage in place, key concern..."></textarea>
            <span class="hint sensitive-warning">Please do not include Social Security numbers, financial account information, medical records, or other sensitive personal information.</span>
          </div>
          <div class="checkbox">
            <input id="di_consent" name="consent" type="checkbox" required />
            <label for="di_consent">I agree to be contacted by Mischa Wright Insurance Agency about my request. Message and data rates may apply.</label>
          </div>
          <div class="form-status" role="status" aria-live="polite"></div>
          <button type="submit" class="btn btn-primary" data-label="Request a Quote">Request a Quote <span class="arrow" aria-hidden="true">→</span></button>
        </form>
      </div>
    </div>
  </div>
</section>
'''
    render(
        path="disability-insurance.html",
        title="Disability Insurance | Individual Income Protection | Mischa Wright Insurance Agency",
        description="Individual disability insurance for professionals and business owners. Own-occupation definitions, business overhead expense, buy-sell funding. Get a real quote through a short conversation.",
        body=body, active="", depth=0,
    )


STATES = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware","District of Columbia","Florida","Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana","Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania","Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah","Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]

def _state_options():
    return "\n".join(f'<option>{s}</option>' for s in STATES)
