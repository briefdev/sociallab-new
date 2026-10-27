(() => {
  'use strict';

  // TODO: sales WhatsApp number, international format, digits only (e.g. 9665XXXXXXXX).
  // Left empty, wa.me opens WhatsApp and lets the visitor pick the contact.
  const WHATSAPP_NUMBER = '';

  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => [...c.querySelectorAll(s)];
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- Header state ---------- */
  const header = $('.site-header');
  const onScroll = () => header.classList.toggle('scrolled', window.scrollY > 10);
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  $('#year').textContent = new Date().getFullYear();

  /* ---------- Mobile sticky CTA: after the hero, hidden over the form ---------- */
  const sticky = $('#sticky-cta');
  if ('IntersectionObserver' in window) {
    let pastHero = false;
    let demoInView = false;
    const update = () => {
      const show = pastHero && !demoInView;
      sticky.classList.toggle('show', show);
      sticky.setAttribute('aria-hidden', String(!show));
      sticky.tabIndex = show ? 0 : -1;
    };
    new IntersectionObserver(([e]) => { pastHero = !e.isIntersecting; update(); }).observe($('.hero'));
    new IntersectionObserver(([e]) => { demoInView = e.isIntersecting; update(); }).observe($('#demo'));
  }

  /* ---------- Plans: monthly / yearly prices ---------- */
  const billingBtns = $$('[data-billing]');
  billingBtns.forEach((btn) => btn.addEventListener('click', () => {
    const yearly = btn.dataset.billing === 'yearly';
    billingBtns.forEach((b) => {
      b.classList.toggle('on', b === btn);
      b.setAttribute('aria-pressed', String(b === btn));
    });
    $$('.price b[data-monthly]').forEach((b) => { b.textContent = yearly ? b.dataset.yearly : b.dataset.monthly; });
    $$('[data-period]').forEach((el) => { el.textContent = yearly ? 'شهرياً، تُدفع سنوياً' : 'شهرياً'; });
  }));

  // Plan buttons carry the plan name into the demo request
  $$('a[data-plan]').forEach((a) => a.addEventListener('click', () => { $('#f-plan').value = a.dataset.plan; }));

  /* ---------- Demo form -> WhatsApp ---------- */
  const form = $('#demo-form');
  const formError = $('#form-error');
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const required = ['name', 'store', 'phone'].map((n) => form.elements[n]);
    const empty = required.filter((f) => !f.value.trim());
    required.forEach((f) => f.setAttribute('aria-invalid', String(empty.includes(f))));
    formError.hidden = empty.length === 0;
    if (empty.length) { empty[0].focus(); return; }

    const d = Object.fromEntries(new FormData(form));
    const text = [
      'مرحباً سوشل لاب، أرغب بحجز عرض توضيحي.',
      `الاسم: ${d.name.trim()}`,
      `المتجر: ${d.store.trim()}`,
      `المنصة: ${d.platform}`,
      `الجوال: ${d.phone.trim()}`,
      d.plan && `الباقة: ${d.plan}`,
    ].filter(Boolean).join('\n');
    window.open(`https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(text)}`, '_blank', 'noopener');
  });

  /* ---------- Motion (GSAP) ---------- */
  // Without GSAP or with reduced motion, the page stays in its final, static state.
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

    /* Hero: headline lines, then the arrow draws behind */
    const heroIn = gsap.timeline({ defaults: { ease: 'power3.out' } });
    heroIn
      .from('.hero-title .line', { y: 28, autoAlpha: 0, duration: .6, stagger: .12 })
      .from('.hero .eyebrow, .lead, .hero-actions, .works-with', { y: 12, autoAlpha: 0, duration: .45, stagger: .06 }, '-=.3');
    const [swooshBody, swooshTip] = $$('.hero-swoosh .draw');
    heroIn.add(draw(swooshBody, { duration: 1.4 }), .2);
    heroIn.add(draw(swooshTip, { duration: .5, ease: 'power2.out' }), 1.45);

    /* Hero chat: the conversation plays once when the phone is visible */
    const chat = $('.chat');
    chat.classList.add('seq');
    const step = (n) => $(`[data-step="${n}"]`, chat);
    const reveal = (tl, el, at) => {
      tl.call(() => el.style.setProperty('display', ''), null, at);
      tl.call(() => el.removeAttribute('data-step'), null, '<');
      tl.fromTo(el, { autoAlpha: 0, y: 8 }, { autoAlpha: 1, y: 0, duration: .3, ease: 'power2.out' }, '<');
    };
    const chatTl = gsap.timeline({ paused: true });
    reveal(chatTl, step(1), .2);
    reveal(chatTl, step(2), '+=.5');
    chatTl.set(step(2), { display: 'none' }, '+=1.1');
    reveal(chatTl, step(3), '<');
    reveal(chatTl, step(4), '+=1.1');
    reveal(chatTl, step(5), '+=.8');
    ScrollTrigger.create({ trigger: '.phone', start: 'top 85%', once: true, onEnter: () => chatTl.play() });

    /* Problem: the story is read line by line */
    gsap.from('.story li, .story-turn', {
      autoAlpha: 0, y: 18, duration: .5, stagger: .35, ease: 'power2.out',
      scrollTrigger: { trigger: '.story', start: 'top 75%' },
    });

    /* Abandoned-cart flow */
    const steps = $$('.step');
    const stepsList = $('.steps');
    const chartLine = $('.chart-line');
    const chartTip = $('.chart-head-arrow');
    const chartArea = $('.chart-area');
    const counter = $('.chart-num [data-count]');
    const target = Number(counter.dataset.count);
    const fmt = (v) => Math.round(v).toLocaleString('en-US');
    stepsList.classList.add('steps-live');
    const setStep = (n) => steps.forEach((s, i) => s.classList.toggle('on', i < n));
    setStep(1);

    const mm = gsap.matchMedia();

    // Desktop: pin the section and let scroll drive the scenario
    mm.add('(min-width: 960px) and (min-height: 700px)', () => {
      drawable(chartLine);
      drawable(chartTip);
      gsap.set(chartArea, { autoAlpha: 0 });
      counter.textContent = '0';
      const tl = gsap.timeline({
        scrollTrigger: {
          trigger: '.flow', start: 'top top', end: '+=1400', scrub: .6, pin: true,
          onUpdate: (self) => {
            setStep(Math.min(4, Math.floor(self.progress * 4) + 1));
            counter.textContent = fmt(target * gsap.utils.clamp(0, 1, (self.progress - .5) / .45));
          },
        },
      });
      tl.to(chartLine, { strokeDashoffset: 0, autoAlpha: 1, duration: 1, ease: 'none' })
        .to(chartArea, { autoAlpha: 1, duration: .3 }, .55)
        .to(chartTip, { strokeDashoffset: 0, autoAlpha: 1, duration: .15 }, .9);
      return () => { setStep(1); counter.textContent = fmt(target); };
    });

    // Mobile: no pinning, each step lights up as it scrolls in
    mm.add('(max-width: 959px), (max-height: 699px)', () => {
      const triggers = steps.map((s, i) => ScrollTrigger.create({
        trigger: s, start: 'top 80%', onEnter: () => setStep(Math.max(i + 1, 1)),
      }));
      const tl = gsap.timeline({ scrollTrigger: { trigger: '.chart-card', start: 'top 75%', once: true } });
      tl.add(draw(chartLine, { duration: 1.2 }))
        .add(draw(chartTip, { duration: .3 }), '-=.1')
        .from(chartArea, { autoAlpha: 0, duration: .4 }, .5)
        .fromTo({ v: 0 }, { v: 0 }, { v: target, duration: 1.2, ease: 'power2.out', onUpdate() { counter.textContent = fmt(this.targets()[0].v); } }, 0);
      return () => triggers.forEach((t) => t.kill());
    });

    /* Stats: count up once when they scroll in (suffix in <small> is kept) */
    $$('.stat b[data-count]').forEach((b) => {
      const node = b.firstChild;
      const prefix = b.dataset.prefix || '';
      const o = { v: 0 };
      gsap.to(o, {
        v: Number(b.dataset.count), duration: 1.2, ease: 'power2.out',
        scrollTrigger: { trigger: b, start: 'top 85%' },
        onUpdate: () => { node.nodeValue = prefix + fmt(o.v); },
      });
    });

    /* Section headings: one short rise, not every element */
    $$('.ai .h2, .features-title, .int-copy .h2, .plans-head .h2, .faq .h2, .bubble .h2').forEach((h) => {
      gsap.from(h, { y: 16, autoAlpha: 0, duration: .5, ease: 'power2.out', scrollTrigger: { trigger: h, start: 'top 85%' } });
    });

    /* AI chat: messages arrive in order */
    gsap.from('.ai-window > *', {
      autoAlpha: 0, y: 10, duration: .35, stagger: .3, ease: 'power2.out',
      scrollTrigger: { trigger: '.ai-window', start: 'top 75%' },
    });

    /* Bento tiles + report bars */
    gsap.from('.tile', {
      autoAlpha: 0, y: 16, duration: .45, stagger: .08, ease: 'power2.out',
      scrollTrigger: { trigger: '.bento', start: 'top 80%' },
    });
    gsap.from('.bars span', {
      scaleY: 0, duration: .5, stagger: .05, ease: 'power2.out',
      scrollTrigger: { trigger: '.bars', start: 'top 85%' },
    });

    /* Integrations hub: platforms connect to the core */
    gsap.from('.hub .node', {
      autoAlpha: 0, scale: .9, duration: .35, stagger: .1, ease: 'back.out(1.6)',
      scrollTrigger: { trigger: '.hub', start: 'top 75%' },
    });

    /* Plans: the arrow climbs the steps */
    const stairsLine = $('.stairs-line .draw');
    const stairsTl = gsap.timeline({ scrollTrigger: { trigger: '.stairs', start: 'top 75%' } });
    stairsTl.from('.plan', { autoAlpha: 0, y: 20, duration: .45, stagger: .12, ease: 'power2.out' });
    if (getComputedStyle(stairsLine.ownerSVGElement).display !== 'none') {
      stairsTl.add(draw(stairsLine, { duration: 1.1 }), .1);
    }

    /* Demo bubble: the logo arrow completes over the form */
    const [bubbleBody, bubbleTip] = $$('.bubble-arrow .draw');
    const bubbleTl = gsap.timeline({ scrollTrigger: { trigger: '.bubble', start: 'top 75%' } });
    bubbleTl.add(draw(bubbleBody, { duration: .9 })).add(draw(bubbleTip, { duration: .35, ease: 'power2.out' }), '-=.1');
  };

  // GSAP scripts are deferred and load before this file; fonts can shift layout, so refresh once they settle.
  init();
  if (document.fonts && window.ScrollTrigger) document.fonts.ready.then(() => window.ScrollTrigger.refresh());
})();
