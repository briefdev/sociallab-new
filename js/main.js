(() => {
  'use strict';

  const SALES_WHATSAPP = '966530901484';

  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => [...c.querySelectorAll(s)];
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const fmt = (v) => Math.round(v).toLocaleString('en-US');

  /* ---------- Header: scrolled state ---------- */
  const header = $('.site-header');
  const onScroll = () => header.classList.toggle('scrolled', window.scrollY > 10);
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  $$('[data-year]').forEach((el) => { el.textContent = new Date().getFullYear(); });

  /* ---------- Platform dropdown (desktop) ---------- */
  const dd = $('.dd');
  if (dd) {
    const btn = $('.dd-btn', dd);
    const panel = $('.dd-panel', dd);
    const setOpen = (open) => {
      btn.setAttribute('aria-expanded', String(open));
      panel.hidden = !open;
    };
    btn.addEventListener('click', () => setOpen(panel.hidden));
    if (window.matchMedia('(hover: hover)').matches) {
      let t;
      dd.addEventListener('mouseenter', () => { clearTimeout(t); setOpen(true); });
      dd.addEventListener('mouseleave', () => { t = setTimeout(() => setOpen(false), 150); });
    }
    document.addEventListener('click', (e) => { if (!dd.contains(e.target)) setOpen(false); });
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && !panel.hidden) { setOpen(false); btn.focus(); } });
  }

  /* ---------- Mobile menu ---------- */
  const menuBtn = $('.menu-btn');
  const mnav = $('#mnav');
  if (menuBtn && mnav) {
    const setMenu = (open) => {
      menuBtn.setAttribute('aria-expanded', String(open));
      menuBtn.setAttribute('aria-label', open ? 'إغلاق القائمة' : 'فتح القائمة');
      mnav.hidden = !open;
      document.body.classList.toggle('menu-open', open);
      header.classList.toggle('menu-is-open', open);
    };
    menuBtn.addEventListener('click', () => setMenu(mnav.hidden));
    $$('a', mnav).forEach((a) => a.addEventListener('click', () => setMenu(false)));
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && !mnav.hidden) { setMenu(false); menuBtn.focus(); } });
    window.matchMedia('(min-width: 1024px)').addEventListener('change', (m) => { if (m.matches) setMenu(false); });
  }

  /* ---------- Pricing: monthly / yearly ---------- */
  const billingBtns = $$('[data-billing]');
  billingBtns.forEach((btn) => btn.addEventListener('click', () => {
    const yearly = btn.dataset.billing === 'yearly';
    billingBtns.forEach((b) => {
      b.classList.toggle('on', b === btn);
      b.setAttribute('aria-pressed', String(b === btn));
    });
    $$('.plan [data-monthly]').forEach((el) => {
      if (el.dataset.yearly) el.textContent = yearly ? el.dataset.yearly : el.dataset.monthly;
    });
    $$('.plan').forEach((plan) => {
      const hasYearly = !!$('[data-yearly]', plan);
      const period = $('[data-period]', plan);
      if (period) period.textContent = yearly && hasYearly ? '/ سنة' : '/ شهر';
    });
    $$('[data-alt]').forEach((el) => {
      el.dataset.text ??= el.textContent;
      el.textContent = yearly ? 'شهران مجاناً' : el.dataset.text;
    });
  }));

  /* ---------- Pricing: plan tabs drive the swipeable list on mobile ---------- */
  const planTabs = $$('[data-plan-tab]');
  const planList = $('.plan-list');
  if (planTabs.length && planList) {
    const select = (key) => planTabs.forEach((t) => t.setAttribute('aria-selected', String(t.dataset.planTab === key)));
    planTabs.forEach((t) => t.addEventListener('click', () => {
      select(t.dataset.planTab);
      $(`#plan-${t.dataset.planTab}`).scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'nearest', inline: 'center' });
    }));
    // Keep the active tab in sync while swiping
    const io = new IntersectionObserver((entries) => {
      entries.forEach((en) => { if (en.isIntersecting) select(en.target.id.replace('plan-', '')); });
    }, { root: planList, threshold: 0.6 });
    $$('.plan', planList).forEach((p) => io.observe(p));
  }

  /* ---------- Demo form -> WhatsApp (sales) ---------- */
  const form = $('#demo-form');
  if (form) {
    const formError = $('#form-error');
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const required = ['name', 'store', 'url', 'phone'].map((n) => form.elements[n]).filter(Boolean);
      const empty = required.filter((f) => !f.value.trim());
      required.forEach((f) => f.setAttribute('aria-invalid', String(empty.includes(f))));
      formError.hidden = empty.length === 0;
      if (empty.length) { empty[0].focus(); return; }

      const d = Object.fromEntries(new FormData(form));
      const text = [
        'مرحباً سوشل لاب، أرغب بتجربة وكيل مدرّب على متجري.',
        `الاسم: ${d.name.trim()}`,
        `المتجر: ${d.store.trim()}`,
        `رابط المتجر: ${d.url.trim()}`,
        `المنصة: ${d.platform}`,
        `الجوال: ${d.phone.trim()}`,
      ].join('\n');
      window.open(`https://wa.me/${SALES_WHATSAPP}?text=${encodeURIComponent(text)}`, '_blank', 'noopener');
    });
  }

  /* ---------- Demo simulator: scripted conversations ---------- */
  const simChat = $('#sim-chat');
  if (simChat) {
    // Illustrative scripts; each line is [who, text, tag?]
    const SCENARIOS = {
      product: {
        name: 'متجرك', status: 'يرد تلقائياً', channel: 'واتساب',
        lines: [
          ['in', 'السلام عليكم، العباية السوداء مقاس M متوفرة؟'],
          ['out', 'وعليكم السلام! متوفرة. أضيفها لسلتك؟', 'وكيل الذكاء الاصطناعي'],
          ['in', 'إيه أكيد'],
          ['card', 'تم إنشاء الطلب #10482'],
        ],
      },
      cart: {
        name: 'متجرك', status: 'تذكير تلقائي', channel: 'واتساب',
        lines: [
          ['sys', 'سلة متروكة في المتجر · سلة'],
          ['out', 'أهلاً! منتجاتك ما زالت في السلة. تحب نكمل طلبك؟', 'تذكير تلقائي'],
          ['in', 'إيه، كمّلوه'],
          ['card', 'العميل أكمل الطلب'],
        ],
      },
      cod: {
        name: 'وكيل المكالمات الذكي', status: 'مكالمة صادرة', channel: 'اتصال',
        lines: [
          ['sys', 'طلب جديد بالدفع عند الاستلام'],
          ['out', 'مرحباً، معك متجرك. نتصل لتأكيد طلبك بالدفع عند الاستلام.', 'وكيل المكالمات'],
          ['in', 'إيه، أكدوه لو سمحت.'],
          ['out', 'تم التأكيد. يوصلك الطلب قريباً.', 'وكيل المكالمات'],
          ['card', 'الطلب مؤكد'],
        ],
      },
      comment: {
        name: 'حساب متجرك', status: 'رد على تعليق', channel: 'إنستقرام',
        lines: [
          ['sys', 'تعليق جديد على منشورك'],
          ['in', 'كم السعر؟'],
          ['out', 'أهلاً بك! أرسلنا لك التفاصيل في الرسائل الخاصة.', 'رد ذكي على التعليق'],
          ['card', 'وصلت رسالة خاصة للعميل'],
        ],
      },
    };
    const okIcon = '<span class="ok"><svg class="i" viewBox="0 0 24 24"><path d="m5 12 5 5 9-10"/></svg></span>';
    const node = ([who, text, tag]) => {
      const el = document.createElement('div');
      if (who === 'card') {
        el.className = 'order-card';
        el.innerHTML = `${okIcon}<div><strong></strong></div>`;
        el.querySelector('strong').textContent = text;
      } else if (who === 'sys') {
        el.className = 'sys mono';
        el.textContent = text;
      } else {
        el.className = `msg ${who}`;
        if (tag) { const t = document.createElement('em'); t.className = 'ai-tag mono'; t.textContent = tag; el.append(t); }
        el.append(document.createTextNode(text));
      }
      return el;
    };

    let timers = [];
    let current = 'product';
    const play = (key) => {
      current = key;
      timers.forEach(clearTimeout);
      timers = [];
      const s = SCENARIOS[key];
      $('[data-sim-name]').textContent = s.name;
      $('[data-sim-status]').textContent = s.status;
      $('[data-sim-channel]').textContent = s.channel;
      simChat.replaceChildren();
      if (reduce) { s.lines.forEach((l) => simChat.append(node(l))); return; }
      let t = 300;
      s.lines.forEach((l) => {
        if (l[0] === 'out') {
          timers.push(setTimeout(() => {
            const ty = document.createElement('div');
            ty.className = 'typing typing-out';
            ty.innerHTML = '<span></span><span></span><span></span>';
            simChat.append(ty);
          }, t));
          t += 900;
          timers.push(setTimeout(() => { $('.typing', simChat)?.remove(); simChat.append(node(l)); }, t));
        } else {
          timers.push(setTimeout(() => simChat.append(node(l)), t));
        }
        t += 900;
      });
    };
    const tabs = $$('[data-scenario]');
    tabs.forEach((tab) => tab.addEventListener('click', () => {
      tabs.forEach((x) => x.setAttribute('aria-selected', String(x === tab)));
      play(tab.dataset.scenario);
    }));
    $('[data-sim-replay]').addEventListener('click', () => play(current));
    // Show the first conversation right away, then play it when the phone scrolls into view
    SCENARIOS[current].lines.forEach((l) => simChat.append(node(l)));
    new IntersectionObserver((entries, obs) => {
      if (entries[0].isIntersecting) { play(current); obs.disconnect(); }
    }, { threshold: 0.3 }).observe(simChat);
  }

  /* ---------- Motion (GSAP) ---------- */
  // Without GSAP or with reduced motion, every page stays in its final, static state.
  const init = () => {
    if (reduce || !window.gsap || !window.ScrollTrigger) return;
    const { gsap, ScrollTrigger } = window;
    gsap.registerPlugin(ScrollTrigger);

    // Stroke-draw helper: pathLength=1 makes every path draw the same way at any size
    const drawable = (path) => {
      path.setAttribute('pathLength', '1');
      gsap.set(path, { strokeDasharray: 1, strokeDashoffset: 1, autoAlpha: 0 });
      return path;
    };
    const draw = (path, vars = {}) =>
      gsap.to(drawable(path), { strokeDashoffset: 0, autoAlpha: 1, duration: 1.2, ease: 'power2.inOut', ...vars });
    const onArrive = (trigger, fn, start = 'top 80%') =>
      ScrollTrigger.create({ trigger, start, once: true, onEnter: fn });

    /* Home hero: headline lines, then the arrow draws behind */
    if ($('.hero-title')) {
      const heroIn = gsap.timeline({ defaults: { ease: 'power3.out' } });
      heroIn
        .from('.hero-title .line', { y: 28, autoAlpha: 0, duration: .6, stagger: .12 })
        .from('.hero .eyebrow, .hero .lead, .hero-chips, .hero-actions, .works-with', { y: 12, autoAlpha: 0, duration: .45, stagger: .06 }, '-=.3');
      const [body, tip] = $$('.hero-swoosh .draw');
      heroIn.add(draw(body, { duration: 1.4 }), .2);
      heroIn.add(draw(tip, { duration: .5, ease: 'power2.out' }), 1.45);
    }

    /* Inner page heroes: title rises, side arrow draws */
    if ($('.page-title')) {
      gsap.from('.page-hero .crumbs, .page-hero .eyebrow, .page-title, .page-hero .lead, .page-hero .hero-actions, .feat-stat', { y: 16, autoAlpha: 0, duration: .5, stagger: .07, ease: 'power2.out' });
      $$('.page-swoosh .draw').forEach((p) => draw(p, { duration: 1.3, delay: .2 }));
    }

    /* Home hero chat: plays once when visible */
    const chat = $('.hero .chat');
    if (chat) {
      chat.classList.add('seq');
      const step = (n) => $(`[data-step="${n}"]`, chat);
      const reveal = (tl, el, at) => {
        tl.call(() => el.style.setProperty('display', ''), null, at);
        tl.call(() => el.removeAttribute('data-step'), null, '<');
        tl.fromTo(el, { autoAlpha: 0, y: 8 }, { autoAlpha: 1, y: 0, duration: .3, ease: 'power2.out' }, '<');
      };
      const tl = gsap.timeline({ paused: true });
      reveal(tl, step(1), .2);
      reveal(tl, step(2), '+=.5');
      tl.set(step(2), { display: 'none' }, '+=1.1');
      reveal(tl, step(3), '<');
      reveal(tl, step(4), '+=1.1');
      reveal(tl, step(5), '+=.8');
      onArrive('.hero .phone', () => tl.play(), 'top 85%');
    }

    /* Problem story: read line by line */
    if ($('.story')) {
      gsap.from('.story li, .story-turn', { autoAlpha: 0, y: 18, duration: .5, stagger: .35, ease: 'power2.out', scrollTrigger: { trigger: '.story', start: 'top 75%' } });
    }

    /* Abandoned-cart steps light up in order on arrival */
    const steps = $$('.steps .step');
    if (steps.length) {
      $('.steps').classList.add('steps-live');
      const setStep = (n) => steps.forEach((s, i) => s.classList.toggle('on', i < n));
      const tl = gsap.timeline({ paused: true });
      steps.forEach((s, i) => tl.call(() => setStep(i + 1), null, i * .45));
      onArrive('.steps', () => tl.play());
    }

    /* Recovered-carts chart draws on arrival */
    const chartLine = $('.chart-line');
    if (chartLine) {
      const tl = gsap.timeline({ scrollTrigger: { trigger: '.chart-card', start: 'top 80%', once: true } });
      tl.add(draw(chartLine, { duration: 1.4 }))
        .add(draw($('.chart-head-arrow'), { duration: .3 }), '-=.1')
        .from('.chart-area', { autoAlpha: 0, duration: .5 }, .6);
    }

    /* Numbers count up once when they scroll in */
    $$('[data-count]').forEach((el) => {
      const o = { v: 0 };
      const end = Number(el.dataset.count);
      gsap.to(o, {
        v: end, duration: 1.3, ease: 'power2.out',
        scrollTrigger: { trigger: el, start: 'top 90%', once: true },
        onUpdate: () => { el.textContent = fmt(o.v); },
      });
    });

    /* Section headings: one short rise */
    $$('main section:not(.hero):not(.page-hero) .h2').forEach((h) => {
      gsap.from(h, { y: 16, autoAlpha: 0, duration: .5, ease: 'power2.out', scrollTrigger: { trigger: h, start: 'top 85%', once: true } });
    });

    /* Groups that arrive together, with a short stagger */
    [
      ['.feature-rows', '.feature-rows li'],
      ['.how-steps', '.how-steps li'],
      ['.caps-list', '.caps-list li'],
      ['.case-grid', '.case-card'],
      ['.rel-grid', '.rel'],
      ['.int-list', '.int-tiles li'],
    ].forEach(([trigger, items]) => {
      if (!$(items)) return;
      gsap.from(items, { autoAlpha: 0, y: 14, duration: .4, stagger: .06, ease: 'power2.out', scrollTrigger: { trigger, start: 'top 80%', once: true } });
    });

    /* Integrations hub: platforms connect to the core */
    if ($('.hub .node')) {
      gsap.from('.hub .node', { autoAlpha: 0, scale: .9, duration: .35, stagger: .08, ease: 'back.out(1.6)', scrollTrigger: { trigger: '.hub', start: 'top 75%', once: true } });
    }

    /* Pricing: the arrow climbs the steps (desktop only, where it is shown) */
    const stairsLine = $('.stairs-line .draw');
    if (stairsLine && getComputedStyle(stairsLine.ownerSVGElement).display !== 'none') {
      const tl = gsap.timeline({ scrollTrigger: { trigger: '.stairs', start: 'top 75%', once: true } });
      tl.from('.plan', { autoAlpha: 0, y: 20, duration: .45, stagger: .12, ease: 'power2.out' })
        .add(draw(stairsLine, { duration: 1.1 }), .1);
    }

    /* Logo bubbles: the arrow completes over the CTA */
    $$('.bubble-arrow').forEach((svg) => {
      const [body, tip] = $$('.draw', svg);
      const tl = gsap.timeline({ scrollTrigger: { trigger: svg.parentElement, start: 'top 75%', once: true } });
      tl.add(draw(body, { duration: .9 })).add(draw(tip, { duration: .35, ease: 'power2.out' }), '-=.1');
    });
  };

  // GSAP scripts are deferred and load before this file; fonts can shift layout, so refresh once they settle.
  init();
  if (document.fonts && window.ScrollTrigger) document.fonts.ready.then(() => window.ScrollTrigger.refresh());
})();
