"""Homepage."""

def build(render, img_slot, CAL, GR, RAMSEY):
    body = f'''
<section class="hero">
  <div class="wrap">
    <div class="hero-grid">
      <div>
        <span class="eyebrow">Independent Long-Term Care Insurance Guidance</span>
        <h1>Long-Term Care Planning, Explained in Plain English.</h1>
        <p class="lede">Independent guidance on Long-Term Care Insurance, annuities, and life insurance. Education first. We start with a short conversation so any quote reflects your age, state, health, and goals.</p>
        <div class="btn-row">
          <a class="btn btn-primary btn-lg" href="start.html?ref=hero">Start Here <span class="arrow" aria-hidden="true">→</span></a>
        </div>
        <p class="supporting">We will help you choose the right starting point based on the type of insurance guidance you need.</p>
      </div>
      <div class="hero-media">
        <span class="hero-badge">RamseyTrusted LTC Pro</span>
        {img_slot("images/generated/home-hero.jpg", "Couple in their sixties reviewing planning documents at a bright kitchen table")}
      </div>
    </div>
  </div>
</section>

<aside class="trust-strip" aria-label="At a glance">
  <div class="wrap">
    <ul>
      <li>CLTC&reg; advisor</li>
      <li>Long-Term Care specialist</li>
      <li>Independent agency</li>
      <li>100% virtual planning</li>
      <li>Nevada based, licensed team nationwide</li>
    </ul>
  </div>
</aside>

<section class="alt">
  <div class="wrap">
    <div class="grid-2 narrow-side">
      <div class="headshot-wrap">
        <div class="headshot-frame">
          {img_slot("images/headshot/mischa-wright-headshot.jpg", "Mischa Wright, founder of Mischa Wright Insurance Agency")}
        </div>
      </div>
      <div>
        <span class="eyebrow">Meet your advisor</span>
        <h2>Mischa Wright, CLTC&reg;</h2>
        <p>Mischa is a Long-Term Care insurance producer, advisor, and educator. His connection to this work is personal: his Opa lived with Parkinson&rsquo;s disease, and the family experienced firsthand the emotional, practical, and financial weight of extended care.</p>
        <p>That experience shaped a simple conviction. Families deserve clear guidance and a plan <em>before</em> care becomes a crisis. Clients work directly with Mischa and are supported by a team of licensed insurance professionals serving families nationwide.</p>
        <div class="btn-row mt-2">
          <a class="btn btn-ghost" href="about.html">More about Mischa</a>
          <a class="btn btn-ghost" href="{GR}" target="_blank" rel="noopener">Read our Google Reviews</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="dark">
  <div class="wrap-mid statement">
    <span class="quote-mark" aria-hidden="true">&ldquo;</span>
    <h2>Long-term care planning is not about fear. It is about keeping choices open, protecting the people around you, and making decisions calmly before you have to.</h2>
    <p style="max-width:56ch; margin:0 auto;">Roughly 70% of Americans turning 65 today will need some form of long-term care during their lives, according to the U.S. Department of Health and Human Services. Medicare does not cover the ongoing custodial care most families end up needing.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div style="max-width:640px; margin-bottom: 48px;">
      <span class="eyebrow">How we help</span>
      <h2>A flagship specialty in Long-Term Care, supported by the retirement tools that surround it.</h2>
    </div>

    <div class="service-lead" style="margin-bottom:24px">
      <span class="tag">Flagship specialty</span>
      <h3>Long-Term Care Insurance</h3>
      <p>Traditional LTC, hybrid life/LTC, asset-based, and annuity-linked strategies. Underwriting, benefit design, inflation protection, elimination periods, shared care, Partnership-qualified policies. We walk through the mechanics before we discuss numbers.</p>
      <a class="btn btn-primary" href="long-term-care-insurance.html">Explore Long-Term Care <span class="arrow" aria-hidden="true">→</span></a>
    </div>

    <div class="grid-2 tight-gap">
      <div class="service-secondary">
        <h3>Annuities</h3>
        <p>Retirement income planning, principal-protection strategies, and income riders (some with long-term care features).</p>
        <a class="more" href="annuities.html">See annuity options</a>
      </div>
      <div class="service-secondary">
        <h3>Life Insurance</h3>
        <p>Term, permanent, and hybrid life/LTC designs, matched to what the money is actually supposed to do.</p>
        <a class="more" href="life-insurance.html">See life insurance options</a>
      </div>
    </div>

    <div class="service-minor">
      <h3>Medicare (referral)</h3>
      <p>Our licensed team can help connect you with appropriate Medicare Supplement, Advantage, or Part D guidance.</p>
      <a class="more" href="medicare.html">Request Medicare help</a>
    </div>
    <div class="service-minor">
      <h3>Disability Insurance</h3>
      <p>Individual disability coverage for professionals and business owners. Own-occupation definitions, business-overhead expense, buy-sell funding.</p>
      <a class="more" href="disability-insurance.html">Request a disability quote</a>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="grid-2 wide-side">
      <div>
        <span class="eyebrow">The independent advantage</span>
        <h2>We are not tied to a single carrier.</h2>
        <p>As an independent agency, we compare designs from multiple highly rated insurance companies and match the plan to what you actually need rather than what one company happens to sell.</p>
        <p>That matters most in Long-Term Care, where the same health picture can be declined by one carrier and approved by another. Part of our job is quietly matching your situation to the carrier most likely to say yes, before a formal application creates a record.</p>
      </div>
      <div>
        <ol class="steps stack" style="counter-reset: step;">
          <li class="step">
            <h3>You bring the situation</h3>
            <p>Age, state, health picture, existing coverage, and what you are trying to protect.</p>
          </li>
          <li class="step">
            <h3>We bring the options</h3>
            <p>Side-by-side comparisons across appropriate carriers, in plain language, with the trade-offs stated honestly.</p>
          </li>
          <li class="step">
            <h3>You decide</h3>
            <p>Apply only if it makes sense. Our job is to guide, not to sell.</p>
          </li>
        </ol>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap-mid center">
    <span class="eyebrow">Trusted by clients nationwide</span>
    <h2>Real reviews from real families we have worked with.</h2>
    <p class="lede" style="margin: 0 auto 32px; max-width: 60ch;">We do not display testimonial quotations without written approval. See what our clients have said in their own words on Google.</p>
    <div class="reviews-band" style="text-align:left; max-width: 780px; margin: 0 auto;">
      <div class="reviews-icon" aria-hidden="true">G</div>
      <div>
        <h3>Read what our clients say on Google</h3>
        <p class="stars" aria-label="Five star reviews"><span aria-hidden="true">&#9733;&#9733;&#9733;&#9733;&#9733;</span></p>
      </div>
      <a class="btn btn-primary" href="{GR}" target="_blank" rel="noopener">Read our Google Reviews <span class="arrow" aria-hidden="true">→</span></a>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div style="max-width:640px; margin-bottom: 40px;">
      <span class="eyebrow">Recent guides</span>
      <h2>Learn how it works before you decide anything.</h2>
    </div>
    <div class="post-grid">
      <article class="post-card">
        <div class="thumb"><img src="images/blog/ltc-covers-thumb.jpg" alt="Adult daughter and mother reviewing paperwork calmly at a kitchen table" loading="lazy" width="1280" height="720" /></div>
        <div class="body">
          <span class="cat">Long-Term Care</span>
          <h3>What Long-Term Care Insurance actually covers</h3>
          <p>The specific care settings, monthly benefits, and services a modern LTC policy pays for, and where the coverage stops.</p>
          <a class="read" href="blog/what-long-term-care-insurance-covers.html">Read the guide</a>
        </div>
      </article>
      <article class="post-card">
        <div class="thumb"><img src="images/blog/medicare-vs-ltc-thumb.jpg" alt="Senior man at a desk reading Medicare enrollment information" loading="lazy" width="1280" height="720" /></div>
        <div class="body">
          <span class="cat">Long-Term Care</span>
          <h3>Medicare vs. Long-Term Care Insurance</h3>
          <p>A common misunderstanding worth clearing up: what Medicare does and does not pay for when ongoing care is needed.</p>
          <a class="read" href="blog/medicare-vs-long-term-care-insurance.html">Read the guide</a>
        </div>
      </article>
      <article class="post-card">
        <div class="thumb"><img src="images/blog/when-to-buy-thumb.jpg" alt="Couple in their fifties walking a tree-lined path in autumn" loading="lazy" width="1280" height="720" /></div>
        <div class="body">
          <span class="cat">Long-Term Care</span>
          <h3>When should you buy LTC insurance?</h3>
          <p>Why age, health, and market timing all matter, and how the &ldquo;planning window&rdquo; opens and closes.</p>
          <a class="read" href="blog/when-should-you-buy-long-term-care-insurance.html">Read the guide</a>
        </div>
      </article>
    </div>
  </div>
</section>

<section>
  <div class="wrap-mid">
    <div class="center mb-2">
      <span class="eyebrow">Common questions</span>
      <h2>Questions we hear most often.</h2>
    </div>
    <div class="faq">
      <details>
        <summary>Does Medicare pay for long-term care?</summary>
        <div class="answer"><p>Medicare covers limited skilled care and short-term rehabilitation after a qualifying hospital stay. It does not cover the ongoing custodial care that most long-term care claims involve, help with bathing, dressing, eating, and supervision for cognitive decline.</p></div>
      </details>
      <details>
        <summary>How much does Long-Term Care Insurance cost?</summary>
        <div class="answer"><p>Premiums vary widely by age at application, health, state, benefit design, and policy type. A meaningful design at 55 costs substantially less than the same design at 65, which is one of several reasons planning is easier to do earlier than later. Illustrative pricing examples live in our <a href="blog/how-much-does-long-term-care-insurance-cost.html">cost guide</a>.</p></div>
      </details>
      <details>
        <summary>Is the first call free?</summary>
        <div class="answer"><p>Yes. There is no charge for an initial conversation and no obligation to apply.</p></div>
      </details>
      <details>
        <summary>Are you licensed in my state?</summary>
        <div class="answer"><p>Mischa is Nevada based, and our licensed team supports clients nationwide. During the first call we confirm licensure specifics for your state and the products you are considering.</p></div>
      </details>
    </div>
    <div class="center mt-3">
      <a class="btn btn-ghost" href="faq.html">See all frequently asked questions</a>
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="wrap-mid">
    <h2>The first conversation is short, honest, and free.</h2>
    <p>We will help you understand your options, decide what makes sense, and never push you toward anything that does not.</p>
    <a class="btn btn-invert btn-lg" href="start.html?ref=cta-band">Start Here <span class="arrow" aria-hidden="true">→</span></a>
  </div>
</section>
'''
    schema = [{
      "@context": "https://schema.org",
      "@type": "InsuranceAgency",
      "name": "Mischa Wright Insurance Agency",
      "url": "https://mrwrightinsures.com",
      "logo": "https://mrwrightinsures.com/images/favicon-512.png",
      "image": "https://mrwrightinsures.com/images/og-image.jpg",
      "description": "Independent Long-Term Care Insurance guidance, annuities, life insurance, Medicare referrals, and disability coverage. Education-first, 100% virtual, licensed team nationwide.",
      "telephone": "+1-858-345-9952",
      "email": "Mischa@MrWrightInsures.com",
      "areaServed": {"@type": "Country", "name": "United States"},
      "address": {"@type": "PostalAddress", "addressRegion": "NV", "addressCountry": "US"},
      "founder": {"@type": "Person", "name": "Mischa Wright", "honorificSuffix": "CLTC", "jobTitle": "Long-Term Care Insurance Advisor"},
      "knowsAbout": ["Long-Term Care Insurance", "Annuities", "Life Insurance", "Medicare", "Disability Insurance"],
      "slogan": "We serve, not sell."
    }]
    render(
      path="index.html",
      schema=schema,
      title="Mischa Wright Insurance Agency | Long-Term Care Insurance & Retirement Protection",
      description="Independent Long-Term Care Insurance guidance from Mischa Wright, CLTC. Education-first planning for LTC, annuities, life insurance, Medicare referrals, and disability coverage. 100% virtual, licensed team nationwide.",
      body=body,
      active="home",
      depth=0,
    )
