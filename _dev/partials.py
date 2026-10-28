"""Shared page parts: head, header, footer, CTA band. {R} is replaced with the path to the site root."""

LINKS = {
    'register': 'https://sociallab.sa/authentication/side-register',
    'login': 'https://sociallab.sa/authentication/login',
    'calendly': 'https://calendly.com/getsociallab/getsociallab',
    'wa': 'https://wa.me/966530901484',
    'appstore': 'https://apps.apple.com/sa/app/social-lab-grow-your-business/id6745023855',
    'play': 'https://play.google.com/store/apps/details?id=com.social.lab.app',
    'channel': 'https://whatsapp.com/channel/0029VbBZ3Oa8F2pIwcq7J43s',
    'partners': 'https://s.sociallab.sa/landing.html',
    'blog': 'https://blog.sociallab.sa/',
    'help': 'https://sociallab.sa/help',
    'privacy': 'https://sociallab.sa/privacy',
    'terms': 'https://sociallab.sa/terms',
    'sbc': 'https://eauthenticate.saudibusiness.gov.sa/certificate-details/0000206830',
}

ICONS = {
    'inbox': '<path d="M3 13h5l2 3h4l2-3h5"/><path d="M5.5 5h13l2.5 8v6a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1v-6z"/>',
    'whatsapp': '<path d="M4 20l1.3-3.9A8 8 0 1 1 8 19.3z"/><path d="M9 10c.5 2 2 3.5 4 4l1.2-1.2 2 1-.6 1.6c-3.4.2-7-3.4-6.8-6.8L10.4 8l1 2z"/>',
    'automation': '<rect x="4" y="3" width="6" height="5" rx="1"/><rect x="14" y="16" width="6" height="5" rx="1"/><rect x="4" y="16" width="6" height="5" rx="1"/><path d="M7 8v8M7 12h8a2 2 0 0 1 2 2v2"/>',
    'ai': '<path d="M12 3l1.8 4.7 4.7 1.8-4.7 1.8L12 16l-1.8-4.7L5.5 9.5l4.7-1.8z"/><path d="M19 15l.8 2.2 2.2.8-2.2.8L19 21l-.8-2.2-2.2-.8 2.2-.8z"/>',
    'campaigns': '<path d="M3 10v4h3l7 4V6l-7 4z"/><path d="M16.5 9a4 4 0 0 1 0 6M19 6.5a8 8 0 0 1 0 11"/>',
    'call': '<path d="M4 14v-2a8 8 0 0 1 16 0v2"/><path d="M4 14h3v5H5a1 1 0 0 1-1-1zM20 14h-3v5h2a1 1 0 0 0 1-1z"/><path d="M17 19c0 1.5-1.5 2-3 2h-2"/>',
    'tickets': '<path d="M4 6h16v4a2 2 0 0 0 0 4v4H4v-4a2 2 0 0 0 0-4z"/><path d="M14 6v12" stroke-dasharray="2 2"/>',
    'orders': '<path d="M5 8h14l-1.2 12H6.2z"/><path d="M9 8V6.5a3 3 0 0 1 6 0V8"/>',
    'app': '<rect x="7" y="2.5" width="10" height="19" rx="2"/><path d="M11 18.5h2"/>',
    'check': '<path d="m5 12 5 5 9-10"/>',
    'arrow': '<path d="M19 12H5m6-6-6 6 6 6"/>',
    'chev': '<path d="m6 9 6 6 6-6"/>',
    'plug': '<path d="M9 3v5M15 3v5M6 8h12v3a6 6 0 0 1-12 0zM12 17v4"/>',
    'chart': '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
    'cases': '<path d="M4 7h16v12H4z"/><path d="M9 7V5h6v2M4 12h16"/>',
}


def icon(name, cls='i'):
    return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true">{ICONS[name]}</svg>'


ARROW = icon('arrow', 'i i-dir')



def store_badges(root):
    # Official badges from Apple and Google, unmodified
    return f'''<div class="store-badges">
        <a class="store-badge" href="{LINKS['appstore']}" target="_blank" rel="noopener"><img src="{root}assets/img/appstore-badge.svg" alt="حمّله من App Store" width="144" height="48" loading="lazy"></a>
        <a class="store-badge" href="{LINKS['play']}" target="_blank" rel="noopener"><img src="{root}assets/img/googleplay-badge.png" alt="احصل عليه من Google Play" width="161" height="48" loading="lazy"></a>
      </div>'''


def head(title, desc, root):
    return f'''<!doctype html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="theme-color" content="#0C221C">
  <meta name="color-scheme" content="dark">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="ar_SA">
  <meta property="og:site_name" content="سوشل لاب">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="{root}assets/img/mark.png">
  <link rel="icon" type="image/png" href="{root}assets/img/favicon.png">
  <link rel="apple-touch-icon" href="{root}assets/img/favicon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Alexandria:wght@500;700;800&family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans+Arabic:wght@400;500;600&display=swap">
  <link rel="stylesheet" href="{root}css/style.css">
  <!-- Analytics: add GTM (GTM-5ZHL5MGD) here when ready -->
</head>
<body>

<!-- Signature shape: the growth arrow that cuts the logo bubble -->
<svg width="0" height="0" class="sr-only" aria-hidden="true">
  <defs>
    <linearGradient id="swoosh-fade" x1="0" y1="1" x2="1" y2="0">
      <stop offset="0" stop-color="#66AE66" stop-opacity="0"/>
      <stop offset=".45" stop-color="#66AE66" stop-opacity=".55"/>
      <stop offset="1" stop-color="#D9F27E"/>
    </linearGradient>
  </defs>
</svg>

<a class="skip" href="#main">تخطَّ إلى المحتوى</a>
'''


def header(root, features, active=''):
    def cur(key):
        return ' aria-current="page"' if key == active else ''

    dd_items = '\n'.join(
        f'''            <a class="dd-item" href="{root}features/{f['slug']}.html"{cur(f['slug'])}>
              <span class="dd-ic">{icon(f['icon'])}</span>
              <span><strong>{f['nav']}</strong><small>{f['nav_desc']}</small></span>
            </a>''' for f in features)
    m_items = '\n'.join(
        f'''        <a href="{root}features/{f['slug']}.html"{cur(f['slug'])}>{icon(f['icon'])}{f['nav']}</a>''' for f in features)
    platform_active = ' is-active' if active in [f['slug'] for f in features] else ''
    return f'''
<header class="site-header" id="top">
  <div class="wrap header-in">
    <a class="brand" href="{root}index.html" aria-label="سوشل لاب — الرئيسية">
      <img src="{root}assets/img/logo-light.png" alt="سوشل لاب" width="768" height="207">
    </a>
    <nav class="nav" aria-label="التنقل الرئيسي">
      <div class="dd">
        <button class="dd-btn{platform_active}" type="button" aria-expanded="false" aria-controls="dd-platform">المنصة {icon('chev')}</button>
        <div class="dd-panel" id="dd-platform" hidden>
          <div class="dd-grid">
{dd_items}
          </div>
          <a class="dd-foot" href="{root}integrations.html">{icon('plug')} يتصل بكل أدواتك: 18 تكاملاً مع متجرك وأنظمتك {ARROW}</a>
        </div>
      </div>
      <a href="{root}integrations.html"{cur('integrations')}>التكاملات</a>
      <a href="{root}case-studies.html"{cur('cases')}>دراسات الحالة</a>
      <a href="{root}pricing.html"{cur('pricing')}>الباقات</a>
      <a href="{root}faq.html"{cur('faq')}>الأسئلة</a>
    </nav>
    <div class="header-actions">
      <a class="login" href="{LINKS['login']}">دخول</a>
      <a class="btn btn-lime btn-sm" href="{root}demo.html">جرّب على متجرك</a>
      <button class="menu-btn" type="button" aria-expanded="false" aria-controls="mnav" aria-label="فتح القائمة"><span></span><span></span></button>
    </div>
  </div>
  <div class="mnav" id="mnav" hidden>
    <div class="wrap">
      <p class="mnav-label mono">المنصة</p>
      <div class="mnav-features">
{m_items}
      </div>
      <div class="mnav-links">
        <a href="{root}integrations.html"{cur('integrations')}>التكاملات</a>
        <a href="{root}case-studies.html"{cur('cases')}>دراسات الحالة</a>
        <a href="{root}pricing.html"{cur('pricing')}>الباقات</a>
        <a href="{root}faq.html"{cur('faq')}>الأسئلة الشائعة</a>
        <a href="{LINKS['login']}">تسجيل الدخول</a>
      </div>
      <a class="btn btn-lime btn-block" href="{root}demo.html">جرّب سوشل لاب على متجرك</a>
    </div>
  </div>
</header>
'''


def cta_band(root):
    return f'''
  <!-- Closing CTA inside the logo bubble -->
  <section class="cta-band" aria-labelledby="cta-title">
    <div class="wrap">
      <div class="bubble bubble-cta">
        <svg class="bubble-arrow" viewBox="0 0 300 300" aria-hidden="true">
          <path class="draw" d="M0 300 C 110 270, 200 190, 238 52" fill="none" stroke="#D9F27E" stroke-width="16" stroke-linecap="round"/>
          <path class="draw draw-late" d="M205 78 L240 40 L276 108" fill="none" stroke="#D9F27E" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        <div>
          <h2 id="cta-title" class="h2">جاهز تزيد <span>مبيعاتك؟</span></h2>
          <p class="body">سوشل لاب يعمل عنك. احجز جلستك المجانية الآن ونبني لك النظام خطوة بخطوة.</p>
        </div>
        <div class="cta-actions">
          <a class="btn btn-lime" href="{LINKS['calendly']}" target="_blank" rel="noopener">احجز جلسة مجانية {ARROW}</a>
          <a class="btn btn-line" href="{root}demo.html">جرّب على متجرك</a>
          <p class="cta-note">بدون بطاقة ائتمان • إعداد في 10 دقائق</p>
        </div>
      </div>
    </div>
  </section>
'''


SOCIAL = [
    ('https://www.instagram.com/Getsociallab', 'انستقرام', '<svg viewBox="0 0 24 24" aria-hidden="true" class="ic-stroke"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.3" cy="6.7" r=".9" class="dot-fill"/></svg>'),
    ('https://www.tiktok.com/@getsocial.lab', 'تيك توك', '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12.525.02c1.31-.02 2.61-.01 3.91-.02.08 1.53.63 3.09 1.75 4.17 1.12 1.11 2.7 1.62 4.24 1.79v4.03c-1.44-.05-2.89-.35-4.2-.97-.57-.26-1.1-.59-1.62-.93-.01 2.92.01 5.84-.02 8.75-.08 1.4-.54 2.79-1.35 3.94-1.31 1.92-3.58 3.17-5.91 3.21-1.43.08-2.86-.31-4.08-1.03-2.02-1.19-3.44-3.37-3.65-5.71-.02-.5-.03-1-.01-1.49.18-1.9 1.12-3.72 2.58-4.96 1.66-1.44 3.98-2.13 6.15-1.72.02 1.48-.04 2.96-.04 4.44-.99-.32-2.15-.23-3.02.37-.63.41-1.11 1.04-1.36 1.75-.21.51-.15 1.07-.14 1.61.24 1.64 1.82 3.02 3.5 2.87 1.12-.01 2.19-.66 2.77-1.61.19-.33.4-.67.41-1.06.1-1.79.06-3.57.07-5.36.01-4.03-.01-8.05.02-12.07z"/></svg>'),
    ('https://x.com/Getsociallab', 'إكس', '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M18.901 1.153h3.68l-8.04 9.19L24 22.846h-7.406l-5.8-7.584-6.638 7.584H.474l8.6-9.83L0 1.154h7.594l5.243 6.932ZM17.61 20.644h2.039L6.486 3.24H4.298Z"/></svg>'),
    ('https://www.linkedin.com/company/sociallabsa/', 'لينكدإن', '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.064 2.064 0 1 1 0-4.128 2.064 2.064 0 0 1 0 4.128zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>'),
    ('https://www.youtube.com/@getsociallab', 'يوتيوب', '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>'),
]


def footer(root, features):
    feat_links = '\n'.join(f'        <a href="{root}features/{f["slug"]}.html">{f["nav"]}</a>' for f in features)
    social = '\n'.join(f'      <a href="{u}" target="_blank" rel="noopener" aria-label="{n}">{s}</a>' for u, n, s in SOCIAL)
    return f'''
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-top">
      <div class="footer-brand">
        <img src="{root}assets/img/logo-light.png" alt="سوشل لاب" width="768" height="207" loading="lazy">
        <p>منصة متكاملة لإدارة التواصل مع العملاء عبر واتساب وإنستقرام وتيك توك.</p>
        {store_badges(root)}
      </div>
      <nav class="footer-col" aria-label="المنصة">
        <p class="footer-h">المنصة</p>
{feat_links}
      </nav>
      <nav class="footer-col" aria-label="روابط">
        <p class="footer-h">سوشل لاب</p>
        <a href="{root}integrations.html">التكاملات</a>
        <a href="{root}case-studies.html">دراسات الحالة</a>
        <a href="{root}pricing.html">الباقات والأسعار</a>
        <a href="{root}demo.html">جرّب على متجرك</a>
        <a href="{root}faq.html">الأسئلة الشائعة</a>
        <a href="{LINKS['help']}">مركز المعرفة</a>
        <a href="{LINKS['blog']}">المدونة</a>
        <a href="{LINKS['partners']}">انضم إلى شركاء وسفراء سوشل لاب</a>
      </nav>
      <div class="footer-col">
        <p class="footer-h">تواصل معنا</p>
        <a href="{LINKS['wa']}" target="_blank" rel="noopener">واتساب: <span class="mono" dir="ltr">+966 53 090 1484</span></a>
        <a href="{LINKS['calendly']}" target="_blank" rel="noopener">احجز جلسة مجانية</a>
        <a href="{LINKS['channel']}" target="_blank" rel="noopener">انضم إلى مجتمعنا</a>
        <nav class="footer-social" aria-label="حساباتنا على وسائل التواصل">
{social}
        </nav>
      </div>
    </div>
    <div class="footer-bottom">
      <p class="copy mono">© <span data-year>2026</span> سوشل لاب. جميع الحقوق محفوظة.</p>
      <div class="footer-legal">
        <a href="{LINKS['privacy']}">الخصوصية</a>
        <a href="{LINKS['terms']}">الشروط والأحكام</a>
        <a href="{LINKS['sbc']}" target="_blank" rel="noopener">موثّق في المركز السعودي للأعمال</a>
      </div>
    </div>
  </div>
</footer>

<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js" defer></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js" defer></script>
<script src="{root}js/main.js" defer></script>
</body>
</html>
'''
