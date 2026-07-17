"""About, Process, FAQ, Contact, Resources, Privacy, Disclosures, 404."""
from pages_services import _state_options

def build(render, img_slot, CAL, GR, RAMSEY):
    _about(render, img_slot, CAL, GR, RAMSEY)
    _process(render, img_slot, CAL)
    _faq(render, img_slot, CAL)
    _contact(render, img_slot, CAL)
    _resources(render, img_slot, CAL)
    _privacy(render)
    _disclosures(render, RAMSEY)
    _four_oh_four(render)


def _about(render, img_slot, CAL, GR, RAMSEY):
    body = f'''
<section class="hero">
  <div class="wrap">
    <div class="grid-2 narrow-side">
      <div class="headshot-wrap">
        <div class="headshot-frame">
          {img_slot("images/headshot/mischa-wright-headshot.jpg", "Mischa Wright, CLTC, founder of Mischa Wright Insurance Agency")}
        </div>
      </div>
      <div>
        <span class="eyebrow">About</span>
        <h1>Mischa Wright, CLTC&reg;</h1>
        <p class="lede">Long-Term Care insurance producer, advisor, and educator. Founder of Mischa Wright Insurance Agency.</p>
        <div style="margin-top: 20px;">
          <span class="credential">CLTC&reg; Certification in Long-Term Care</span>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap-mid">
    <span class="eyebrow">Why this work</span>
    <h2>The plan you make now is a gift to the family you will not have to figure it out with later.</h2>
    <p>My connection to long-term care planning is personal. My Opa lived with Parkinson&rsquo;s disease. Our family experienced firsthand the emotional, practical, and financial reality of extended care. We learned in real time how choices narrow when a plan has not been made in advance.</p>
    <p>That experience shaped a simple conviction: families deserve clear guidance and a plan before care becomes a crisis. Not to sell insurance. To make the conversation possible.</p>
  </div>
</section>

<section>
  <div class="wrap-mid">
    <span class="eyebrow">How the agency works</span>
    <h2>Independent, education-first, and 100% virtual.</h2>
    <p>Mischa Wright Insurance Agency is an independent agency. We are not tied to a single carrier, which means we can compare designs across multiple highly rated insurance companies and match the plan to what you actually need.</p>
    <p>Clients work directly with Mischa and are supported by a team of licensed insurance professionals serving families nationwide. We meet by phone and video, at times that work for you, from wherever you are.</p>
    <p><a href="{RAMSEY}" target="_blank" rel="noopener">Mischa is a RamseyTrusted Long-Term Care Pro</a> and CLTC&reg; advisor. We do not display carrier logos on this site.</p>
  </div>
</section>

<section class="alt">
  <div class="wrap-mid">
    <span class="eyebrow">A few words on tone</span>
    <h2>&ldquo;We serve, not sell.&rdquo;</h2>
    <p>You will not be pressured on the first call. You will not be pressured on the last call either. When something we could sell you would not actually help you, we say so and part as friends.</p>
    <p>Our goal is that the first conversation is genuinely useful whether or not you become a client. That is the whole practice.</p>
    <div class="btn-row mt-2">
      <a class="btn btn-primary" href="start.html?ref=about">Start Here <span class="arrow" aria-hidden="true">→</span></a>
      <a class="btn btn-ghost" href="{GR}" target="_blank" rel="noopener">Read our Google Reviews</a>
    </div>
  </div>
</section>
'''
    schema = [{
      "@context": "https://schema.org",
      "@type": "Person",
      "name": "Mischa Wright",
      "honorificSuffix": "CLTC",
      "jobTitle": "Long-Term Care Insurance Producer, Advisor, and Educator",
      "worksFor": {"@type": "InsuranceAgency", "name": "Mischa Wright Insurance Agency", "url": "https://mrwrightinsures.com"},
      "url": "https://mrwrightinsures.com/about",
      "email": "Mischa@MrWrightInsures.com",
      "telephone": "+1-858-345-9952",
      "knowsAbout": ["Long-Term Care Insurance", "Annuities", "Life Insurance", "Disability Insurance"],
      "address": {"@type": "PostalAddress", "addressRegion": "NV", "addressCountry": "US"}
    }]
    render(path="about.html",
        schema=schema,
        title="About Mischa Wright, CLTC | Mischa Wright Insurance Agency",
        description="Mischa Wright is a CLTC-certified Long-Term Care insurance advisor. His personal connection to LTC planning through his Opa's Parkinson's disease shapes an education-first practice.",
        body=body, active="about", depth=0)


def _process(render, img_slot, CAL):
    steps = [
        ("Short intro call", "A 15-minute conversation to understand what prompted your call and confirm this is a fit. No obligation."),
        ("Working session", "A longer conversation. Age, state, health picture, existing coverage, and what you are trying to protect."),
        ("Research", "We research strategies and carriers that match your specific situation and health picture."),
        ("Side-by-side review", "We walk through comparisons in plain language, with trade-offs stated honestly. You take notes, we answer questions."),
        ("Apply if it makes sense", "Only if it does. There is no obligation to apply, and we will tell you honestly if a design does not fit."),
        ("Guide the underwriting", "We guide and coordinate the underwriting process, help gather any medical information the carrier needs, and answer questions along the way."),
        ("Policy delivery review", "When the policy arrives, we walk through what you have and answer questions before you sign."),
        ("Stay available", "We stay available for future questions, annual reviews, and life changes that affect what you own."),
    ]
    step_html = "".join(f'<li class="step"><h3>{t}</h3><p>{d}</p></li>' for t, d in steps)

    body = f'''
<section class="hero">
  <div class="wrap-mid">
    <span class="eyebrow">Our process</span>
    <h1>Eight steps, taken at your pace.</h1>
    <p class="lede">The process is designed to make good decisions unhurried. Some clients complete it in a week. Others take a season. Both are fine.</p>
  </div>
</section>

<section class="alt">
  <div class="wrap-mid">
    <ol class="steps" style="counter-reset: step;">
      {step_html}
    </ol>
  </div>
</section>

<section class="cta-band">
  <div class="wrap-mid">
    <h2>Start with a short conversation.</h2>
    <p>The first call is 15 minutes. There is no cost and no obligation to apply for anything after.</p>
    <a class="btn btn-invert btn-lg" href="{CAL["general"]}" target="_blank" rel="noopener">Book a 15-Minute Call <span class="arrow" aria-hidden="true">→</span></a>
  </div>
</section>
'''
    render(path="process.html",
        title="Our Process | Mischa Wright Insurance Agency",
        description="An eight-step, education-first insurance planning process. Short intro call, working session, research, side-by-side comparison, and ongoing support.",
        body=body, active="", depth=0)


def _faq(render, img_slot, CAL):
    cats = [
        ("Long-Term Care", [
            ("What does Long-Term Care Insurance cover?",
             "Policies fund ongoing help with daily activities: home care, assisted living, memory care, skilled nursing, and adult day services. Benefits are paid when you cannot perform a set number of activities of daily living or need supervision because of cognitive decline."),
            ("Does Medicare pay for long-term care?",
             "Medicare covers limited skilled care and short-term rehabilitation after a qualifying hospital stay. It does not cover the ongoing custodial care that most long-term care claims involve."),
            ("When should I buy LTC insurance?",
             "The best window is when you are healthy enough to qualify and young enough that pricing is reasonable, generally the mid-50s to early 60s for many people. Waiting past that window closes some doors."),
            ("Is it ever too late?",
             "It can be, in the sense that health changes may take traditional or hybrid coverage off the table. Even then, annuity-based strategies or self-funding plans can often still be structured usefully."),
            ("What health issues affect approval?",
             "Cognitive and memory concerns are the most sensitive area. Mobility, recent major medical events, and current use of assistance for daily activities are also weighted heavily. Well-managed conditions like blood pressure or cholesterol are routinely insurable."),
            ("How much does LTC insurance cost?",
             "Premiums vary widely by age, health, state, benefit design, and policy type. Our cost guide has illustrative examples."),
            ("Why do you need to talk before giving me a quote?",
             "Because a real quote depends on your age, state, and health. Numbers without those facts are guesses and are usually misleading."),
            ("What is an elimination period?",
             "A time-based deductible measured in days. You cover care during that period; then benefits begin. Longer elimination periods reduce the premium."),
            ("What is inflation protection?",
             "An option that grows your monthly benefit over time so a policy purchased today still pays a meaningful share of care 20 years from now."),
            ("What is shared care?",
             "Available on many joint policies. Lets spouses draw from each other's benefit pool if one person's claim runs long."),
            ("Traditional vs hybrid vs asset-based, in one sentence each?",
             "Traditional: ongoing premiums for the deepest care coverage per dollar. Hybrid: life insurance with an LTC engine inside, so someone always benefits. Asset-based: repositions a lump-sum of savings into a dedicated LTC pool with a death benefit if unused."),
            ("Can life insurance help with long-term care?",
             "Yes. Hybrid life/LTC policies and long-term care riders can turn a life insurance benefit into care funding."),
            ("Can annuities help fund long-term care?",
             "Yes. Certain annuities include income doublers or LTC riders. They are often the answer when health closes other doors."),
        ]),
        ("How we work", [
            ("Do you work with multiple insurance companies?",
             "Yes. We are an independent agency and compare designs across multiple highly rated carriers."),
            ("Are you licensed in my state?",
             "Mischa is Nevada based, and our licensed team supports clients nationwide. During the first call we confirm licensure for your state and the products you are considering."),
            ("How does the consultation work?",
             "Everything is virtual by phone and video. The first call is 15 minutes; a working session is longer if the fit is right."),
            ("Is there a cost for the first call?",
             "No. There is no cost and no obligation to apply."),
        ]),
        ("Other insurance", [
            ("Do you help with Medicare?",
             "Yes, through our licensed team. Our Medicare page has a form to request help."),
            ("Is Medicare the same thing as Long-Term Care Insurance?",
             "No. They cover different things. Medicare is hospital and medical coverage plus limited skilled care. Long-Term Care Insurance is the coverage that pays for ongoing custodial care."),
            ("Can you help with Life Insurance, Annuities, and Disability Insurance too?",
             "Yes. We compare designs across multiple highly rated carriers for each of these."),
        ]),
    ]
    parts = []
    for cat, items in cats:
        parts.append(f'<section class="alt"><div class="wrap-mid"><span class="eyebrow">{cat}</span><h2>{cat}</h2><div class="faq">')
        for q, a in items:
            parts.append(f'<details><summary>{q}</summary><div class="answer"><p>{a}</p></div></details>')
        parts.append('</div></div></section>')

    body = f'''
<section class="hero">
  <div class="wrap-mid center">
    <span class="eyebrow">Frequently asked questions</span>
    <h1>Answers, in plain language.</h1>
    <p class="lede">Grouped by topic. Skim what you need, come back for the rest.</p>
  </div>
</section>
{"".join(parts).replace("<section class=\"alt\"><div class=\"wrap-mid\"><span", "<section class=\"alt\"><div class=\"wrap-mid\" style=\"padding-top:8px;\"><span", 1)}
<section class="cta-band">
  <div class="wrap-mid">
    <h2>Have a question we did not answer?</h2>
    <p>Fifteen minutes is usually enough to clear up most things.</p>
    <a class="btn btn-invert btn-lg" href="{CAL["general"]}" target="_blank" rel="noopener">Book a 15-Minute Call <span class="arrow" aria-hidden="true">→</span></a>
  </div>
</section>
'''
    faq_schema = {
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
        for _, items in cats for q, a in items
      ]
    }
    render(path="faq.html",
        schema=[faq_schema],
        title="Frequently Asked Questions | Mischa Wright Insurance Agency",
        description="Answers to the most common Long-Term Care, life insurance, annuity, Medicare, and disability insurance questions we hear from clients.",
        body=body, active="", depth=0)


def _contact(render, img_slot, CAL):
    body = f'''
<section class="hero">
  <div class="wrap-mid">
    <span class="eyebrow">Contact</span>
    <h1>Get in touch.</h1>
    <p class="lede">The first conversation is simply to understand what you are trying to solve. No pressure. No obligation.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="grid-2 narrow-side">
      <div>
        <h2 style="font-size: 1.4rem;">Send a message</h2>
        <form class="form" data-lead-form aria-label="Contact form">
          <input type="hidden" name="source_page" value="/contact" />
          <input type="hidden" name="referrer" value="" />
          <input type="hidden" name="utm_source" value="" />
          <input type="hidden" name="utm_medium" value="" />
          <input type="hidden" name="utm_campaign" value="" />

          <div class="row">
            <div class="field"><label for="c_first">First name</label><input id="c_first" name="first_name" type="text" required /><span class="err-msg">Required</span></div>
            <div class="field"><label for="c_last">Last name</label><input id="c_last" name="last_name" type="text" required /><span class="err-msg">Required</span></div>
          </div>
          <div class="row">
            <div class="field"><label for="c_email">Email</label><input id="c_email" name="email" type="email" required /><span class="err-msg">A valid email is required</span></div>
            <div class="field"><label for="c_phone">Phone</label><input id="c_phone" name="phone" type="tel" required /><span class="err-msg">A valid US phone number is required</span></div>
          </div>
          <div class="field">
            <label for="c_state">State</label>
            <select id="c_state" name="state" required>
              <option value="">Select your state</option>
              {_state_options()}
            </select>
            <span class="err-msg">Required</span>
          </div>
          <div class="field">
            <label for="c_product">What can we help with?</label>
            <select id="c_product" name="product_interest" required>
              <option value="">Choose one</option>
              <option>Long-Term Care Insurance</option>
              <option>Annuities</option>
              <option>Life Insurance</option>
              <option>Medicare</option>
              <option>Disability Insurance</option>
              <option>Not sure yet</option>
            </select>
            <span class="err-msg">Required</span>
          </div>
          <div class="field">
            <label for="c_contact">Preferred contact method</label>
            <select id="c_contact" name="contact_method" required>
              <option value="">Choose one</option>
              <option>Phone</option><option>Email</option><option>Text</option>
            </select>
            <span class="err-msg">Required</span>
          </div>
          <div class="field">
            <label for="c_msg">Message (optional)</label>
            <textarea id="c_msg" name="message" placeholder="A short note about what you're trying to figure out."></textarea>
            <span class="hint sensitive-warning">Please do not include Social Security numbers, financial account information, medical records, or other sensitive personal information.</span>
          </div>
          <div class="checkbox">
            <input id="c_consent" name="consent" type="checkbox" required />
            <label for="c_consent">I agree to be contacted by Mischa Wright Insurance Agency about my request. Message and data rates may apply.</label>
          </div>
          <div class="form-status" role="status" aria-live="polite"></div>
          <button type="submit" class="btn btn-primary" data-label="Send">Send <span class="arrow" aria-hidden="true">→</span></button>
        </form>
      </div>
      <aside class="stack" style="padding-top: 12px;">
        <div>
          <h3 style="font-size: 1rem; margin-bottom: 6px; color: var(--ink-2); text-transform: uppercase; letter-spacing: 0.1em; font-family: var(--sans);">Direct</h3>
          <p style="margin: 0;"><a href="mailto:Mischa@MrWrightInsures.com">Mischa@MrWrightInsures.com</a></p>
          <p style="margin: 0;"><a href="tel:8583459952">858-345-9952</a></p>
        </div>
        <div>
          <h3 style="font-size: 1rem; margin-bottom: 6px; color: var(--ink-2); text-transform: uppercase; letter-spacing: 0.1em; font-family: var(--sans);">Schedule a call</h3>
          <ul style="list-style: none; padding: 0; margin: 0;">
            <li style="margin-bottom: 6px;"><a href="{CAL["general"]}" target="_blank" rel="noopener">15-minute general call</a></li>
            <li style="margin-bottom: 6px;"><a href="{CAL["ltc"]}" target="_blank" rel="noopener">Long-Term Care intro</a></li>
            <li style="margin-bottom: 6px;"><a href="{CAL["annuity"]}" target="_blank" rel="noopener">Annuity intro</a></li>
            <li style="margin-bottom: 6px;"><a href="{CAL["life"]}" target="_blank" rel="noopener">Life insurance intro</a></li>
          </ul>
          <p style="color: var(--ink-2); font-size: 0.9rem; margin-top: 12px;">For Medicare and Disability requests, use the forms on those pages so we can route you to the right specialist.</p>
        </div>
        <div>
          <h3 style="font-size: 1rem; margin-bottom: 6px; color: var(--ink-2); text-transform: uppercase; letter-spacing: 0.1em; font-family: var(--sans);">Service area</h3>
          <p style="color: var(--ink-2); margin: 0;">Nevada based. Licensed team supports clients nationwide. Available Monday through Friday.</p>
        </div>
      </aside>
    </div>
  </div>
</section>
'''
    render(path="contact.html",
        title="Contact | Mischa Wright Insurance Agency",
        description="Get in touch: send a message, schedule a call, or reach us by email or phone. The first conversation has no cost and no obligation.",
        body=body, active="contact", depth=0)


def _resources(render, img_slot, CAL):
    posts = [
        ("what-long-term-care-insurance-covers", "What Long-Term Care Insurance actually covers", "Long-Term Care",
         "The specific care settings, monthly benefits, and services a modern LTC policy pays for, and where the coverage stops.",
         "ltc-covers-thumb.jpg", "Adult daughter and mother reviewing paperwork calmly at a kitchen table"),
        ("medicare-vs-long-term-care-insurance", "Medicare vs. Long-Term Care Insurance", "Long-Term Care",
         "A common misunderstanding worth clearing up: what Medicare does and does not pay for when ongoing care is needed.",
         "medicare-vs-ltc-thumb.jpg", "Senior man at a desk reading Medicare enrollment information"),
        ("when-should-you-buy-long-term-care-insurance", "When should you buy LTC insurance?", "Long-Term Care",
         "Why age, health, and market timing all matter, and how the planning window opens and closes.",
         "when-to-buy-thumb.jpg", "Couple in their fifties walking a tree-lined path in autumn"),
        ("how-much-does-long-term-care-insurance-cost", "How much does Long-Term Care Insurance cost?", "Long-Term Care",
         "The five factors that drive premiums, plus illustrative pricing examples across ages, states, and policy designs.",
         "cost-thumb.jpg", "Woman at a kitchen island reviewing a household budget"),
        ("traditional-vs-hybrid-long-term-care-insurance", "Traditional vs. hybrid vs. annuity-based LTC planning", "Long-Term Care",
         "The three main structures compared, with honest trade-offs and the situations each design fits.",
         "traditional-vs-hybrid-thumb.jpg", "Couple reviewing a policy document with an advisor over video call"),
    ]
    cards = []
    for slug, title, cat, ex, thumb, alt in posts:
        cards.append(f'''<article class="post-card">
      <div class="thumb"><img src="images/blog/{thumb}" alt="{alt}" loading="lazy" width="1280" height="720" /></div>
      <div class="body">
        <span class="cat">{cat}</span>
        <h3>{title}</h3>
        <p>{ex}</p>
        <a class="read" href="blog/{slug}.html">Read the guide</a>
      </div>
    </article>''')

    body = f'''
<section class="hero">
  <div class="wrap-mid">
    <span class="eyebrow">Resources</span>
    <h1>Guides for people planning ahead.</h1>
    <p class="lede">Education-first content on Long-Term Care planning, with new guides added regularly for life insurance, annuities, Medicare, and disability coverage.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="post-grid">
      {"".join(cards)}
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="wrap-mid">
    <h2>Ready to talk it through?</h2>
    <a class="btn btn-invert btn-lg" href="start.html?ref=resources">Start Here <span class="arrow" aria-hidden="true">→</span></a>
  </div>
</section>
'''
    render(path="resources.html",
        title="Resources | Long-Term Care & Retirement Planning Guides",
        description="Long-Term Care Insurance guides: what it covers, Medicare vs. LTC, when to buy, cost, and how the main policy designs compare.",
        body=body, active="resources", depth=0)


def _privacy(render):
    body = '''
<section class="hero">
  <div class="wrap-mid">
    <span class="eyebrow">Legal</span>
    <h1>Privacy Policy</h1>
    <p class="lede">Effective: June 2026.</p>
  </div>
</section>
<section>
  <div class="article-body">
    <p>Mischa Wright Insurance Agency ("we," "us," "the agency") respects the privacy of visitors and clients. This policy describes what we collect, how we use it, and the choices you have.</p>

    <h2>Information we collect</h2>
    <p>We collect information you provide directly, information about your use of this site, and information from third-party services we use.</p>
    <ul>
      <li><strong>Information you provide:</strong> name, email, phone, state, product interest, preferred contact method, and any message you send when you use a contact form or schedule a call.</li>
      <li><strong>Usage information:</strong> the pages you view, the CTAs you click, the referring source, and general device and browser information collected through analytics.</li>
      <li><strong>Cookies and similar technologies:</strong> we use a small number of cookies for site functionality and analytics.</li>
    </ul>

    <h2>How we use information</h2>
    <p>We use the information to respond to your requests, schedule appointments, send you information you have requested, and improve the site. Where you have provided contact information and consent, we may follow up about your inquiry by phone, email, or text.</p>

    <h2>Third-party services</h2>
    <p>We use the following third-party services in operating this site. Their handling of information is governed by their own privacy policies.</p>
    <ul>
      <li><strong>Tilda</strong> (site hosting and form handling)</li>
      <li><strong>Calendly</strong> (appointment scheduling)</li>
      <li><strong>Google Workspace</strong>, including Google Sheets (lead storage) and Google Analytics 4 (site usage)</li>
      <li><strong>Email delivery</strong> providers used to send our notifications and responses</li>
    </ul>

    <h2>Sharing</h2>
    <p>We do not sell personal information. We share information with service providers as needed to operate the site and respond to inquiries, and with insurance carriers when required to process an application you have authorized.</p>

    <h2>Data retention</h2>
    <p>We retain lead and client information as long as needed to serve you and to comply with legal and regulatory recordkeeping requirements applicable to insurance producers.</p>

    <h2>Your choices</h2>
    <p>You can request that we update or delete personal information you have provided by contacting us at <a href="mailto:Mischa@MrWrightInsures.com">Mischa@MrWrightInsures.com</a>. If you are a resident of a state with additional privacy rights (for example, California), you may have additional rights under state law, including the right to know what personal information is collected and the right to request deletion.</p>

    <h2>Security</h2>
    <p>We use reasonable administrative, technical, and physical safeguards to protect information. No online system is perfectly secure. Please do not send Social Security numbers, financial account information, medical records, or other sensitive personal information through website forms.</p>

    <h2>Children</h2>
    <p>This site is intended for adults. We do not knowingly collect information from children under 13.</p>

    <h2>Updates</h2>
    <p>We may update this policy from time to time. Material changes will be posted on this page with an updated effective date.</p>

    <h2>Contact</h2>
    <p>Mischa Wright Insurance Agency<br />
    Email: <a href="mailto:Mischa@MrWrightInsures.com">Mischa@MrWrightInsures.com</a><br />
    Phone: <a href="tel:8583459952">858-345-9952</a></p>
  </div>
</section>
'''
    render(path="privacy-policy.html",
        title="Privacy Policy | Mischa Wright Insurance Agency",
        description="Privacy policy for Mischa Wright Insurance Agency: what information we collect, how it is used, third-party services, retention, and your choices.",
        body=body, active="", depth=0)


def _disclosures(render, RAMSEY):
    body = f'''
<section class="hero">
  <div class="wrap-mid">
    <span class="eyebrow">Legal</span>
    <h1>Disclosures</h1>
  </div>
</section>
<section>
  <div class="article-body">
    <h2>Insurance products</h2>
    <p>Insurance products are subject to underwriting. Product availability, benefits, riders, guarantees, and premiums vary by carrier, state, age, health, and product type. The specific contract issued controls, and any illustration is not a promise of coverage.</p>

    <h2>Guarantees</h2>
    <p>Contractual guarantees are backed by the claims-paying ability of the issuing insurance company.</p>

    <h2>Long-Term Care Insurance</h2>
    <p>Traditional Long-Term Care Insurance premiums are not guaranteed level and may increase over time subject to state regulator approval. Hybrid and asset-based designs often include contractual premium terms; the specific policy language controls. Partnership-qualified policy features vary by state.</p>

    <h2>Annuities</h2>
    <p>Annuities are insurance contracts. Certain annuities can provide contractual guarantees, subject to the claims-paying ability of the issuing insurance company. Features vary by product, carrier, state, and rider availability. Withdrawals may be subject to surrender charges and, if taken before age 59½, may be subject to a federal 10% additional tax. Fixed indexed annuities are not direct market participation, and interest credits are subject to caps, spreads, and participation rates. Annuities are not right for everyone.</p>

    <h2>Life Insurance</h2>
    <p>Life insurance is subject to underwriting. Premiums, benefits, and cash-value features vary by policy design and carrier. Loans and withdrawals reduce the death benefit and may have tax consequences.</p>

    <h2>Disability Insurance</h2>
    <p>Disability insurance is subject to underwriting. Eligibility and benefits depend on occupation classification, income, health, and policy design. Tax treatment of benefits depends on how premiums were paid and your specific situation.</p>

    <h2>Medicare</h2>
    <p>We are not affiliated with Medicare or any government agency. Plan availability varies by county and carrier. We do not offer every plan available in your area; any information you receive is limited to the plans we offer. For a complete list, please contact <a href="https://www.medicare.gov" target="_blank" rel="noopener">Medicare.gov</a>, 1-800-MEDICARE (24 hours a day, 7 days a week, TTY users can call 1-877-486-2048), or your local State Health Insurance Assistance Program (SHIP).</p>

    <h2>Tax and legal</h2>
    <p>This site does not provide tax or legal advice. Tax treatment of insurance products depends on your specific situation. Consult qualified tax and legal advisors before making decisions.</p>

    <h2>Licensing</h2>
    <p>Mischa Wright is licensed in Nevada. Our licensed team supports clients nationwide, subject to individual licensing in the applicable state. We confirm licensure for your state during the initial conversation.</p>

    <h2>Third-party trademarks</h2>
    <p>RamseyTrusted&reg; is a trademark of its owner. Our reference to <a href="{RAMSEY}" target="_blank" rel="noopener">RamseyTrusted Long-Term Care Pro</a> designates Mischa Wright&rsquo;s participation in that program and is not an endorsement by any other party. All other trademarks referenced remain the property of their respective owners.</p>

    <h2>Third-party links</h2>
    <p>Links to third-party sites are provided for convenience. We are not responsible for the content, accuracy, or privacy practices of external sites.</p>
  </div>
</section>
'''
    render(path="disclosures.html",
        title="Disclosures | Mischa Wright Insurance Agency",
        description="Insurance disclosures: underwriting, product availability, guarantees, annuity, life, disability, and Medicare disclosures, plus tax, legal, and licensing notes.",
        body=body, active="", depth=0)


def _four_oh_four(render):
    body = '''
<section class="oops">
  <div class="wrap-mid">
    <span class="code" aria-hidden="true">404</span>
    <h1>We could not find that page.</h1>
    <p class="lede">The page you were looking for may have moved. Try one of these instead.</p>
    <div class="btn-row" style="justify-content: center; margin-top: 32px;">
      <a class="btn btn-primary" href="index.html">Home</a>
      <a class="btn btn-ghost" href="long-term-care-insurance.html">Long-Term Care</a>
      <a class="btn btn-ghost" href="contact.html">Contact</a>
    </div>
  </div>
</section>
'''
    render(path="404.html",
        title="Page not found | Mischa Wright Insurance Agency",
        description="The page you were looking for could not be found.",
        body=body, active="", depth=0)
