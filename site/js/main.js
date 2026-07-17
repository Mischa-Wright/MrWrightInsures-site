/* Mischa Wright Insurance Agency — site JS */
(function() {
  'use strict';

  /* ---------- Mobile menu ---------- */
  const hamburger = document.querySelector('.hamburger');
  const mobileMenu = document.querySelector('.mobile-menu');
  if (hamburger && mobileMenu) {
    hamburger.addEventListener('click', () => {
      const open = hamburger.getAttribute('aria-expanded') === 'true';
      hamburger.setAttribute('aria-expanded', String(!open));
      mobileMenu.setAttribute('data-open', String(!open));
      document.body.style.overflow = !open ? 'hidden' : '';
    });
    mobileMenu.addEventListener('click', (e) => {
      if (e.target.tagName === 'A') {
        hamburger.setAttribute('aria-expanded', 'false');
        mobileMenu.setAttribute('data-open', 'false');
        document.body.style.overflow = '';
      }
    });
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && mobileMenu.getAttribute('data-open') === 'true') {
        hamburger.setAttribute('aria-expanded', 'false');
        mobileMenu.setAttribute('data-open', 'false');
        document.body.style.overflow = '';
        hamburger.focus();
      }
    });
  }

  /* ---------- Dropdown ---------- */
  const dropdowns = document.querySelectorAll('.dropdown');
  dropdowns.forEach(dd => {
    const trigger = dd.querySelector('.dropdown-trigger');
    if (!trigger) return;
    trigger.setAttribute('aria-haspopup', 'true');
    trigger.setAttribute('aria-expanded', 'false');
    dd.setAttribute('aria-expanded', 'false');

    const toggle = (open) => {
      dd.setAttribute('aria-expanded', String(open));
      trigger.setAttribute('aria-expanded', String(open));
    };

    trigger.addEventListener('click', (e) => {
      e.stopPropagation();
      const open = dd.getAttribute('aria-expanded') === 'true';
      dropdowns.forEach(other => other.setAttribute('aria-expanded', 'false'));
      toggle(!open);
    });
    dd.addEventListener('mouseenter', () => toggle(true));
    dd.addEventListener('mouseleave', () => toggle(false));
    document.addEventListener('click', (e) => {
      if (!dd.contains(e.target)) toggle(false);
    });
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') toggle(false);
    });
  });

  /* ---------- Service param persistence ----------
     Reads ?service= from URL, stores in sessionStorage,
     and appends to any Calendly / form link that expects it.
  */
  const params = new URLSearchParams(window.location.search);
  const svc = params.get('service');
  if (svc) sessionStorage.setItem('mw_service', svc);
  const currentSvc = sessionStorage.getItem('mw_service');

  // Prefill hidden form fields
  document.querySelectorAll('input[name="product_interest"]').forEach(inp => {
    const preset = inp.getAttribute('data-preset');
    if (preset) inp.value = preset;
    else if (currentSvc && !inp.value) inp.value = mapSvcToLabel(currentSvc);
  });
  document.querySelectorAll('select[name="product_interest"]').forEach(sel => {
    if (currentSvc && !sel.value) {
      const label = mapSvcToLabel(currentSvc);
      const opt = Array.from(sel.options).find(o => o.textContent.toLowerCase().includes(label.toLowerCase().split(' ')[0]));
      if (opt) sel.value = opt.value;
    }
  });

  // Preserve source_page + referrer + UTMs
  document.querySelectorAll('input[name="source_page"]').forEach(inp => {
    if (!inp.value) inp.value = window.location.pathname;
  });
  document.querySelectorAll('input[name="referrer"]').forEach(inp => {
    if (!inp.value) inp.value = document.referrer || '';
  });
  ['utm_source','utm_medium','utm_campaign'].forEach(k => {
    const v = params.get(k);
    if (v) {
      document.querySelectorAll(`input[name="${k}"]`).forEach(inp => { inp.value = v; });
    }
  });

  function mapSvcToLabel(s) {
    return ({
      ltc: 'Long-Term Care Insurance',
      annuities: 'Annuities',
      life: 'Life Insurance',
      medicare: 'Medicare',
      disability: 'Disability Insurance',
      general: 'Not sure yet'
    })[s] || '';
  }

  /* ---------- Form validation & honest submission ---------- */
  const forms = document.querySelectorAll('form[data-lead-form]');
  forms.forEach(form => {
    const status = form.querySelector('.form-status');
    const submitBtn = form.querySelector('button[type="submit"]');

    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      // Reset error states
      form.querySelectorAll('.field, .checkbox').forEach(f => f.classList.remove('error'));
      if (status) { status.style.display = 'none'; status.className = 'form-status'; }

      let hasError = false;
      // Required fields
      form.querySelectorAll('[required]').forEach(inp => {
        const value = (inp.type === 'checkbox') ? inp.checked : inp.value.trim();
        if (!value) {
          hasError = true;
          const wrap = inp.closest('.field, .checkbox');
          if (wrap) wrap.classList.add('error');
        }
      });
      // Email format
      const email = form.querySelector('input[type="email"]');
      if (email && email.value) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!re.test(email.value)) {
          hasError = true;
          email.closest('.field').classList.add('error');
        }
      }
      // Phone format (accept common US formats)
      const phone = form.querySelector('input[type="tel"]');
      if (phone && phone.value) {
        const digits = phone.value.replace(/\D/g, '');
        if (digits.length !== 10 && digits.length !== 11) {
          hasError = true;
          phone.closest('.field').classList.add('error');
        }
      }

      if (hasError) {
        if (status) {
          status.textContent = 'Please correct the highlighted fields.';
          status.classList.add('error');
          status.style.display = 'block';
          status.focus();
        }
        return;
      }

      // Honest submission behavior:
      // If a backend endpoint is configured on the form (data-endpoint),
      // send a real POST. Otherwise, tell the user this is a preview.
      const endpoint = form.getAttribute('data-endpoint');
      if (!endpoint) {
        if (status) {
          status.innerHTML = '<strong>Prototype note:</strong> in the live Tilda deployment this form emails Mischa@MrWrightInsures.com and logs to the Website Leads Google Sheet. No submission was sent from this preview.';
          status.classList.add('error');
          status.style.display = 'block';
        }
        return;
      }

      if (submitBtn) { submitBtn.disabled = true; submitBtn.textContent = 'Sending…'; }
      try {
        const fd = new FormData(form);
        const resp = await fetch(endpoint, { method: 'POST', body: fd });
        if (!resp.ok) throw new Error('Bad response ' + resp.status);
        if (status) {
          status.textContent = 'Thank you. Your message has been received. We will contact you within one business day.';
          status.classList.add('success');
          status.style.display = 'block';
        }
        form.reset();
      } catch (err) {
        if (status) {
          status.textContent = 'Something went wrong sending your message. Please try again or email Mischa@MrWrightInsures.com directly.';
          status.classList.add('error');
          status.style.display = 'block';
        }
      } finally {
        if (submitBtn) { submitBtn.disabled = false; submitBtn.textContent = submitBtn.getAttribute('data-label') || 'Send'; }
      }
    });
  });

  /* ---------- FAQ accessibility (details are keyboard-native; enhance aria) ---------- */
  document.querySelectorAll('.faq details').forEach(d => {
    const s = d.querySelector('summary');
    if (s) {
      s.setAttribute('aria-expanded', d.open ? 'true' : 'false');
      d.addEventListener('toggle', () => s.setAttribute('aria-expanded', d.open ? 'true' : 'false'));
    }
  });

  /* ---------- Chooser cards: preserve service through link ---------- */
  document.querySelectorAll('.chooser-card').forEach(card => {
    card.addEventListener('click', (e) => {
      const svcVal = card.getAttribute('data-service');
      if (svcVal) sessionStorage.setItem('mw_service', svcVal);
    });
  });
})();
