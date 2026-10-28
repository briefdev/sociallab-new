"""Builds the static site into the repo root.

Run:  python3 _dev/build.py
Edit content here (and in features.py / partials.py), never in the generated .html files.
All copy must come from docs/content-inventory.md.
"""
from pathlib import Path

from partials import LINKS, ARROW, icon, head, header, footer, cta_band, store_badges
from features import FEATURES, BY_SLUG, mock

OUT = Path(__file__).resolve().parent.parent

STATS = [  # real figures from the current Social Lab landing page
    ('350', '+', '', 'منشأة تجارية تثق بسوشل لاب'),
    ('12', '<', 'ث', 'يرد على العميل'),
    ('30', '+', '%', 'زيادة في المبيعات'),
    ('35', '', '%', 'سلات تم استرجاعها'),
]

CASES = {
    'multi': {
        'sector': 'حل المتاجر المتعددة', 'name': 'إدارة 12 متجراً من لوحة واحدة',
        'story': 'تاجر إلكتروني يدير 12 متجراً متخصصاً ربطها كلها بسوشل لاب. الآن ذكاء اصطناعي واحد يرد على عملاء كل المتاجر، ويرسل التذكيرات، ويحلل الأداء، من شاشة واحدة.',
        'metrics': [('12', 'متجر تحت إدارة واحدة'), ('+180%', 'زيادة إجمالية في المبيعات'), ('70%', 'توفير في وقت فريق الدعم')],
    },
    'fashion': {'sector': 'متاجر الأزياء', 'name': 'متجر لييلا', 'metric': ('+240%', 'مبيعات خلال 3 أشهر'),
                'quote': 'استرجعنا العديد من السلات المتروكة بدون جهد يدوي'},
    'food': {'sector': 'سلاسل المطاعم', 'name': 'مطاعم الرياض', 'metric': ('98%', 'رضا العملاء'),
             'quote': 'مع الرد الفوري 24 ساعة تغيرت تجربة عملائنا كلياً'},
    'tech': {'sector': 'الإلكترونيات', 'name': 'سوق التقنية', 'metric': ('3x', 'معدل التحويل'),
             'quote': 'التذكيرات الآلية ضاعفت مبيعات الجمعة البيضاء ثلاث مرات'},
}

INTEGRATIONS = [
    ('قنوات التواصل', ['WhatsApp', 'Instagram', 'TikTok', 'Twilio']),
    ('المتاجر الإلكترونية', ['سلة Salla', 'زد Zid', 'Shopify', 'WooCommerce']),
    ('إدارة العملاء والأنظمة', ['Odoo', 'Zoho', 'Salesforce', 'HubSpot']),
    ('الإنتاجية والمواعيد', ['Google Sheets', 'Google Calendar', 'Google Meet', 'Trello']),
    ('الأتمتة والبيانات', ['n8n', 'Firecrawl']),
]

PLANS = [  # real plans, prices include VAT; yearly = two months free
    {'key': 'free', 'ar': 'مجاني', 'en': 'Free', 'desc': 'المنصة كاملة، مجاناً للأبد.', 'm': '0', 'y': None, 'usd': '$0',
     'cta': ('ابدأ مجاناً', LINKS['register']), 'note': 'التسجيل المباشر فقط',
     'quota': ['مستخدم واحد', '1,000 رسالة شهرياً', '1 GB تخزين', '1,000 جهة اتصال'],
     'inc': None,
     'feats': ['جميع القنوات (واتساب، إنستقرام، تيك توك، X)', 'صندوق وارد موحد وردود تلقائية أساسية', 'تقويم ولوحة مهام للفريق', 'دعم ذاتي (وكيل ذكاء اصطناعي)']},
    {'key': 'starter', 'ar': 'البداية', 'en': 'Starter', 'desc': 'لفريق خدمة عملاء صغير.', 'm': '90.85', 'y': '908.50', 'usd': '$24', 'usd_y': '$242',
     'cta': ('اختر البداية', LINKS['register']),
     'quota': ['مستخدمان', '5,000 رسالة شهرياً', '2 GB تخزين', '10,000 جهة اتصال'],
     'inc': 'كل ما في المجانية، بالإضافة إلى:',
     'feats': ['قوالب غنية (أزرار وكاروسيل)', 'أيقونة المحادثة الحية للموقع', 'دعم بشري في ساعات العمل', 'شحن النقاط بالسعر القياسي']},
    {'key': 'growth', 'ar': 'النمو', 'en': 'Growth', 'desc': 'تسويق وتذاكر لعمليات النمو.', 'm': '286.35', 'y': '2,863.50', 'usd': '$76', 'usd_y': '$764',
     'cta': ('اختر النمو', LINKS['register']), 'pick': True,
     'quota': ['3 مستخدمين', '25,000 رسالة شهرياً', '5 GB تخزين', '50,000 جهة اتصال'],
     'inc': 'كل ما في البداية، بالإضافة إلى:',
     'feats': ['حملات واتساب التسويقية', 'نظام التذاكر والمتابعة', 'تحليلات متقدمة وقياس رضا العملاء', 'دعم بأولوية', 'نقاط إضافية 10% عند شحن النقاط']},
    {'key': 'business', 'ar': 'الأعمال', 'en': 'Business', 'desc': 'أتمتة التجارة والتكاملات.', 'm': '688.85', 'y': '6,888.50', 'usd': '$184', 'usd_y': '$1,837',
     'cta': ('اختر الأعمال', LINKS['register']),
     'quota': ['6 مستخدمين', '100,000 رسالة شهرياً', '10 GB تخزين', '100,000 جهة اتصال'],
     'inc': 'كل ما في النمو، بالإضافة إلى:',
     'feats': ['وكيل المكالمات الذكي (الدفع عند الاستلام والسلات المتروكة)', 'الردود الذكية على تعليقات إنستقرام', 'مفاتيح API · Odoo · n8n', 'مدير حساب مخصص + SLA', 'نقاط إضافية 20% عند شحن النقاط']},
]
ENTERPRISE = {'ar': 'مخصص', 'en': 'Enterprise', 'desc': 'مصمم خصيصاً للتوسع الكبير.',
              'quota': ['مستخدمون ورسائل مخصصة', 'تخزين وجهات اتصال مخصصة'],
              'feats': ['تكاملات مخصصة وحلول on-prem', 'اتفاقيات مستوى خدمة مخصصة', 'تأهيل ممتاز للعملاء', 'باقات نقاط تفاوضية']}

FAQ = [
    ('ما هو سوشل لاب؟', 'يجمع سوشل لاب كل قنوات التواصل مع العملاء في منصة واحدة: إدارة المحادثات، والحملات، ومتابعة العملاء، والرد على الرسائل من كل المنصات، مع ذكاء اصطناعي يرد تلقائياً ويحسن تجربة العملاء.'),
    ('لماذا سوشل لاب؟', 'لأنه يرد على عملائك خلال أقل من 12 ثانية، ويذكّرهم بعروضك، ويرجّع السلات المتروكة تلقائياً على واتساب. تثق به أكثر من 350 منشأة تجارية.'),
    ('كيف يعمل؟', 'أنشئ حسابك وفعّله، اربط رقم واتساب وقنواتك، أنشئ أول قالب رسالة، أضف جهات الاتصال، وأرسل أول حملة. وإذا تحب، احجز جلسة مجانية ونبني لك النظام خطوة بخطوة.'),
    ('ما علاقته بالتجارة الإلكترونية؟', 'يتصل بمتجرك على سلة وزد وشوبيفاي وWooCommerce: يرجّع السلات المتروكة، ويذكّر عملاءك بعروضك، وفي باقة الأعمال يتصل وكيل المكالمات الذكي لتأكيد طلبات الدفع عند الاستلام واسترجاع السلات.'),
    ('هل يناسب المتاجر الصغيرة؟', 'نعم، سوشل لاب مصمم ليناسب الجميع، من المشاريع الناشئة الصغيرة وحتى المؤسسات الكبيرة. والباقة المجانية تعطيك المنصة كاملة، مجاناً للأبد.'),
    ('هل أحتاج بطاقة ائتمان للبدء؟', 'لا. تبدأ بدون بطاقة ائتمان، والإعداد في 10 دقائق.'),
    ('كيف أربط رقم واتساب؟', 'معالج تجهيز واتساب API يمر بك خلال 5 إلى 7 دقائق على المتطلبات ويطلع لك خطة عمل. بعدها تنفذ الربط بنفسك بمتابعة الفيديوهات، أو تحجز جلسة يمشي معك فيها فريق سوشل لاب خطوة بخطوة.'),
    ('رقمي مربوط بمزود آخر، هل أقدر أنقله؟', 'نعم. ننقل الرقم عبر ترحيل رسمي (Number Migration) من المزود الحالي إلى سوشل لاب.'),
    ('هل أستطيع متابعة تقارير الأداء؟', 'نعم، لوحات تحكم وتقارير تفاعلية لمتابعة عدد الرسائل، ومعدلات الرد، ومستوى رضا العملاء.'),
    ('هل يوجد تطبيق للجوال؟', 'نعم، تطبيق سوشل لاب متاح على App Store وGoogle Play.'),
]


def page(fname, title, desc, body, active='', root='', cta=True):
    html = head(title, desc, root) + header(root, FEATURES, active) + '\n<main id="main">\n' + body
    if cta:
        html += cta_band(root)
    html += '\n</main>\n' + footer(root, FEATURES)
    path = OUT / fname
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding='utf-8')
    print('built', fname)


def stats_band():
    items = '\n'.join(
        f'''        <div class="stat"><b class="mono" dir="ltr"><span class="pre">{pre}</span><span data-count="{n}">{n}</span><small>{suf}</small></b><span>{label}</span></div>'''
        for n, pre, suf, label in STATS)
    return f'''
  <section class="stats-band" aria-label="سوشل لاب بالأرقام">
    <div class="wrap stats">
{items}
    </div>
  </section>
'''


def case_card(key):
    c = CASES[key]
    return f'''<article class="case-card">
          <p class="case-sector mono">{c['sector']}</p>
          <h3>{c['name']}</h3>
          <p class="case-num"><b class="mono" dir="ltr">{c['metric'][0]}</b><span>{c['metric'][1]}</span></p>
          <blockquote>«{c['quote']}»</blockquote>
        </article>'''


def case_featured():
    c = CASES['multi']
    metrics = '\n'.join(f'<div><b class="mono" dir="ltr">{n}</b><span>{l}</span></div>' for n, l in c['metrics'])
    return f'''<article class="case-feature">
        <div>
          <p class="case-sector mono">{c['sector']}</p>
          <h3>{c['name']}</h3>
          <p class="body">{c['story']}</p>
        </div>
        <div class="case-metrics">
{metrics}
        </div>
      </article>'''


# ---------------------------------------------------------------- home
def home():
    rows = '\n'.join(f'''        <li><a href="features/{f['slug']}.html">
          <span class="row-n mono">{i:02d}</span>
          <span class="row-ic">{icon(f['icon'])}</span>
          <strong>{f['nav']}</strong>
          <span class="row-d">{f['nav_desc']}</span>
          {ARROW}
        </a></li>''' for i, f in enumerate(FEATURES, 1))
    body = f'''
  <!-- HERO -->
  <section class="hero" aria-labelledby="hero-title">
    <svg class="hero-swoosh" viewBox="0 0 600 600" preserveAspectRatio="none" aria-hidden="true">
      <path class="draw" d="M-20 610 C 220 560, 430 380, 520 70" fill="none" stroke="url(#swoosh-fade)" stroke-width="34" stroke-linecap="round"/>
      <path class="draw draw-late" d="M455 120 L520 52 L585 170" fill="none" stroke="#D9F27E" stroke-width="34" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
    <div class="wrap hero-grid">
      <div class="hero-copy">
        <p class="eyebrow mono">واتساب · إنستقرام · تيك توك · X — في صندوق واحد</p>
        <h1 id="hero-title" class="hero-title">
          <span class="line">أتمتة ذكية</span>
          <span class="line hl">تبيع بدلاً عنك.</span>
        </h1>
        <p class="lead">روبوت ذكاء اصطناعي يرد على عملائك، يذكّر عملاءك بعروضك، ويرجّع السلات المتروكة، تلقائياً على واتساب.</p>
        <ul class="hero-chips">
          <li>{icon('check')}ردود فورية</li>
          <li>{icon('check')}استرجاع السلة</li>
          <li>{icon('check')}تذكير بالعروض</li>
        </ul>
        <div class="hero-actions">
          <a class="btn btn-lime" href="{LINKS['register']}">ابدأ مجاناً {ARROW}</a>
          <a class="link-arrow" href="demo.html">جرّب على متجرك</a>
        </div>
        <p class="works-with">بدون بطاقة ائتمان <i>•</i> إعداد في 10 دقائق</p>
      </div>

      <div class="phone-stage">
        <div class="phone" role="img" aria-label="مثال: عميل يسأل عبر واتساب عن منتج، والرد الآلي يجيب وينشئ الطلب">
          <div class="phone-top">
            <img src="assets/img/mark.png" alt="" width="36" height="36">
            <div><strong>متجرك</strong><span class="status"><b class="dot"></b> يرد تلقائياً</span></div>
            <span class="chip mono">واتساب</span>
          </div>
          <div class="chat" aria-hidden="true">
            <p class="day mono">اليوم</p>
            <div class="msg in" data-step="1">السلام عليكم، العباية السوداء مقاس M متوفرة؟<time class="mono">02:14</time></div>
            <div class="typing" data-step="2"><span></span><span></span><span></span></div>
            <div class="msg out" data-step="3"><em class="ai-tag mono">رد آلي</em>وعليكم السلام! متوفرة. أضيفها لسلتك؟<time class="mono">02:14</time></div>
            <div class="msg in" data-step="4">إيه أكيد<time class="mono">02:15</time></div>
            <div class="order-card" data-step="5">
              <span class="ok">{icon('check')}</span>
              <div><strong>تم إنشاء الطلب <span class="mono">#10482</span></strong><span>العباية السوداء · M</span></div>
            </div>
          </div>
          <div class="composer" aria-hidden="true"><span>اكتب رسالة…</span><b></b></div>
        </div>
      </div>
    </div>
  </section>
{stats_band()}
  <!-- CHANNELS -->
  <section class="channels" aria-label="القنوات المدعومة">
    <div class="wrap channels-in">
      <p class="mono label">صندوق رسائل موحد</p>
      <ul>
        <li><span class="mono">01</span> واتساب</li>
        <li><span class="mono">02</span> إنستقرام</li>
        <li><span class="mono">03</span> ماسنجر</li>
        <li><span class="mono">04</span> تيك توك</li>
        <li><span class="mono">05</span> X</li>
        <li><span class="mono">06</span> تيليجرام</li>
        <li><span class="mono">07</span> البريد</li>
        <li><span class="mono">08</span> مراجعات قوقل</li>
      </ul>
    </div>
  </section>

  <!-- PROBLEM: typographic moment -->
  <section class="problem" aria-labelledby="problem-title">
    <div class="wrap">
      <h2 id="problem-title" class="sr-only">ماذا يحدث عندما لا يرد أحد</h2>
      <p class="clock mono" aria-hidden="true">02:14</p>
      <ol class="story">
        <li>سأل عميل عن مقاس.</li>
        <li>لم يرد أحد.</li>
        <li>في الصباح، كان قد اشترى من متجر آخر.</li>
      </ol>
      <p class="story-turn">مع سوشل لاب، <span>عميلك يلقى رداً خلال أقل من 12 ثانية</span> — في أي ساعة.</p>
    </div>
  </section>

  <!-- PLATFORM INDEX -->
  <section class="platform" id="platform" aria-labelledby="platform-title">
    <div class="wrap">
      <div class="section-head">
        <h2 id="platform-title" class="h2">أدوات تبيع وترد عنك. <span>كل أداة مصممة لتوفير وقتك وزيادة إيراداتك.</span></h2>
      </div>
      <ol class="feature-rows">
{rows}
      </ol>
    </div>
  </section>

  <!-- ABANDONED-CART FLOW -->
  <section class="flow" id="flow" aria-labelledby="flow-title">
    <div class="wrap flow-grid">
      <div class="flow-copy">
        <p class="eyebrow mono">استرجاع السلات المتروكة</p>
        <h2 id="flow-title" class="h2">السلة المتروكة ليست خسارة. <span>هي رسالة لم تُرسل بعد.</span></h2>
        <p class="body">اربط متجرك على سلة أو زد، وسوشل لاب يتابع كل سلة متروكة ويذكّر العميل تلقائياً على واتساب.</p>
        <ol class="steps">
          <li class="step"><span class="step-ic">{icon('orders')}</span><div><strong>سلة متروكة</strong><span>تصل من متجرك على سلة أو زد</span></div><em class="mono">14:02</em></li>
          <li class="step"><span class="step-ic">{icon('whatsapp')}</span><div><strong>تذكير تلقائي على واتساب</strong><span>رسالة تذكّر العميل بسلته</span></div><em class="mono">واتساب</em></li>
          <li class="step"><span class="step-ic">{icon('call')}</span><div><strong>وكيل المكالمات يتصل</strong><span>وكيل المكالمات الذكي في باقة الأعمال</span></div><em class="mono">اتصال</em></li>
          <li class="step step-win"><span class="step-ic">{icon('check')}</span><div><strong>العميل أكمل الطلب</strong><span>والمبيعات رجعت لمتجرك</span></div><em class="mono">✓</em></li>
        </ol>
      </div>
      <div class="flow-chart">
        <div class="chart-card">
          <div class="chart-head"><span>سلات تم استرجاعها</span></div>
          <p class="chart-num"><b class="mono"><span data-count="35">35</span>%</b></p>
          <svg class="chart" viewBox="0 0 400 220" aria-hidden="true">
            <g class="grid-lines"><line x1="0" y1="55" x2="400" y2="55"/><line x1="0" y1="110" x2="400" y2="110"/><line x1="0" y1="165" x2="400" y2="165"/></g>
            <path class="chart-area" d="M0 215 C 150 200, 280 140, 352 24 L 400 24 L 400 220 L 0 220 Z"/>
            <path class="draw chart-line" d="M0 215 C 150 200, 280 140, 352 24" fill="none" stroke="url(#swoosh-fade)" stroke-width="7" stroke-linecap="round"/>
            <path class="draw chart-head-arrow" d="M330 34 L353 20 L372 46" fill="none" stroke="#D9F27E" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
          <a class="link-arrow" href="features/campaigns.html">الحملات واسترجاع السلات</a>
        </div>
      </div>
    </div>
  </section>

  <!-- AI AGENT -->
  <section class="ai" id="ai" aria-labelledby="ai-title">
    <div class="wrap ai-grid">
      <div class="ai-copy">
        <p class="eyebrow mono">وكيل الذكاء الاصطناعي</p>
        <h2 id="ai-title" class="h2">يرد خلال 15 ثانية. <span>ويزيد مبيعاتك حتى 30%.</span></h2>
        <ul class="ticks">
          <li>يفهم العميل.</li>
          <li>يحلل المحادثة.</li>
          <li>يتفاعل حسب الاشتراك.</li>
        </ul>
        <a class="link-arrow" href="features/ai-agent.html">تعرّف على وكيل الذكاء الاصطناعي</a>
      </div>
      <div class="ai-demo">{mock('ai-agent', '')}</div>
    </div>
  </section>

  <!-- CASE STUDIES -->
  <section class="cases" aria-labelledby="cases-title">
    <div class="wrap">
      <div class="section-head">
        <h2 id="cases-title" class="h2">تجار تحقق نتائج حقيقية. <span>من متاجر أزياء لسلاسل مطاعم، سوشل لاب يعمل لكل نوع عمل.</span></h2>
        <a class="link-arrow" href="case-studies.html">كل دراسات الحالة</a>
      </div>
      {case_featured()}
      <div class="case-grid">
        {case_card('fashion')}
        {case_card('food')}
        {case_card('tech')}
      </div>
    </div>
  </section>

  <!-- INTEGRATIONS -->
  <section class="integrations" aria-labelledby="int-title">
    <div class="wrap int-grid">
      <div class="int-copy">
        <p class="eyebrow mono">التكاملات</p>
        <h2 id="int-title" class="h2">يتصل بكل <span>أدواتك.</span></h2>
        <p class="body">متجرك أو CRM أو قنوات التواصل، كلها تعمل مع سوشل لاب بدون تعقيد.</p>
        <a class="link-arrow" href="integrations.html">كل التكاملات (18)</a>
      </div>
      <div class="hub hub-8" aria-label="من التكاملات: سلة، زد، شوبيفاي، WooCommerce، Odoo، Zoho، HubSpot، n8n">
        <svg class="hub-lines" viewBox="0 0 400 400" aria-hidden="true">
          <path d="M200 200 L200 40"/><path d="M200 200 L313 87"/><path d="M200 200 L360 200"/><path d="M200 200 L313 313"/>
          <path d="M200 200 L200 360"/><path d="M200 200 L87 313"/><path d="M200 200 L40 200"/><path d="M200 200 L87 87"/>
        </svg>
        <div class="hub-core"><img src="assets/img/mark.png" alt="" width="64" height="64"></div>
        <span class="node" style="left:50%;top:10%">سلة</span>
        <span class="node" style="left:78%;top:22%">زد</span>
        <span class="node" style="left:88%;top:50%">Shopify</span>
        <span class="node" style="left:78%;top:78%">WooCommerce</span>
        <span class="node" style="left:50%;top:90%">Odoo</span>
        <span class="node" style="left:22%;top:78%">Zoho</span>
        <span class="node" style="left:12%;top:50%">HubSpot</span>
        <span class="node" style="left:22%;top:22%">n8n</span>
      </div>
    </div>
  </section>

  <!-- APP + PRICING TEASER -->
  <section class="duo" aria-label="التطبيق والباقات">
    <div class="wrap duo-grid">
      <div class="duo-card">
        <p class="eyebrow mono">التطبيق</p>
        <h2 class="h3">سوشل لاب على جوالك</h2>
        <p class="body">تابع محادثاتك من أي مكان، وخلّ عملاءك يراسلون متجرك من التطبيق.</p>
        {store_badges('')}
      </div>
      <div class="duo-card duo-price">
        <p class="eyebrow mono">الباقات</p>
        <h2 class="h3">باقات لكل مرحلة من مراحل النمو</h2>
        <p class="from"><span>ابدأ من</span><b class="mono">0</b><span>ر.س — المنصة كاملة، مجاناً للأبد.</span></p>
        <a class="link-arrow" href="pricing.html">قارن الباقات</a>
      </div>
    </div>
  </section>
'''
    page('index.html', 'سوشل لاب | أتمتة ذكية تبيع بدلاً عنك',
         'روبوت ذكاء اصطناعي يرد على عملائك، يذكّرهم بعروضك، ويرجّع السلات المتروكة تلقائياً على واتساب. صندوق رسائل موحد لواتساب وإنستقرام وتيك توك وX.',
         body)


# ---------------------------------------------------------------- feature pages
def feature_page(f):
    R = '../'
    steps = '\n'.join(f'''          <li><span class="mono">{i:02d}</span><strong>{t}</strong><p>{d}</p></li>''' for i, (t, d) in enumerate(f['steps'], 1))
    caps = '\n'.join(f'''          <li>{icon('check')}<div><strong>{t}</strong><p>{d}</p></div></li>''' for t, d in f['caps'])
    stat = ''
    if f.get('stat'):
        stat = f'''<p class="feat-stat"><b class="mono" dir="ltr">{f['stat'][0]}</b><span>{f['stat'][1]}</span></p>'''
    case = ''
    if f.get('case'):
        case = f'''
  <section class="feat-case">
    <div class="wrap">
      <p class="eyebrow mono">من نتائج عملائنا</p>
      <div class="case-grid case-grid-1">{case_card(f['case'])}</div>
    </div>
  </section>'''
    related = '\n'.join(f'''        <a class="rel" href="{BY_SLUG[s]['slug']}.html"><span class="row-ic">{icon(BY_SLUG[s]['icon'])}</span><strong>{BY_SLUG[s]['nav']}</strong><span>{BY_SLUG[s]['nav_desc']}</span>{ARROW}</a>''' for s in f['related'])
    body = f'''
  <section class="page-hero feat-hero" aria-labelledby="page-title">
    <svg class="page-swoosh" viewBox="0 0 600 600" preserveAspectRatio="none" aria-hidden="true">
      <path class="draw" d="M-20 610 C 220 560, 430 380, 520 70" fill="none" stroke="url(#swoosh-fade)" stroke-width="22" stroke-linecap="round"/>
    </svg>
    <div class="wrap feat-hero-grid">
      <div class="feat-copy">
        <nav class="crumbs" aria-label="مسار الصفحة"><a href="{R}index.html">الرئيسية</a><span>/</span><span>المنصة</span></nav>
        <p class="eyebrow mono feat-eyebrow">{icon(f['icon'])} {f['title']}</p>
        <h1 id="page-title" class="page-title">{f['h1'][0]} <span>{f['h1'][1]}</span></h1>
        <p class="lead">{f['lead']}</p>
        {stat}
        <div class="hero-actions">
          <a class="btn btn-lime" href="{R}demo.html">جرّب على متجرك {ARROW}</a>
          <a class="link-arrow" href="{LINKS['register']}">ابدأ مجاناً</a>
        </div>
      </div>
      <div class="feat-visual">{mock(f['slug'], R)}</div>
    </div>
  </section>

  <section class="how" aria-labelledby="how-title">
    <div class="wrap">
      <h2 id="how-title" class="h2">كيف يعمل؟</h2>
      <ol class="how-steps how-{len(f['steps'])}">
{steps}
      </ol>
    </div>
  </section>

  <section class="caps" aria-labelledby="caps-title">
    <div class="wrap caps-grid">
      <div class="caps-head">
        <h2 id="caps-title" class="h2">ماذا تحصل <span>في {f['nav']}؟</span></h2>
        <div class="plan-note">
          <p class="mono">في أي باقة؟</p>
          <p>{f['plan']}</p>
          <a class="link-arrow" href="{R}pricing.html">قارن الباقات</a>
        </div>
      </div>
      <ul class="caps-list">
{caps}
      </ul>
    </div>
  </section>
{case}
  <section class="related" aria-labelledby="rel-title">
    <div class="wrap">
      <h2 id="rel-title" class="h3">اكتشف أيضاً</h2>
      <div class="rel-grid">
{related}
      </div>
    </div>
  </section>
'''
    page(f'features/{f["slug"]}.html', f'{f["title"]} | سوشل لاب', f['lead'], body, active=f['slug'], root=R)


# ---------------------------------------------------------------- integrations
def integrations():
    groups = '\n'.join(f'''      <div class="int-group">
        <h2 class="int-h">{g}</h2>
        <ul class="int-tiles">
{chr(10).join(f'          <li><span class="mono" aria-hidden="true">{n.split()[-1][0]}</span>{n}</li>' for n in names)}
        </ul>
      </div>''' for g, names in INTEGRATIONS)
    body = f'''
  <section class="page-hero" aria-labelledby="page-title">
    <div class="wrap">
      <p class="eyebrow mono">التكاملات · 18</p>
      <h1 id="page-title" class="page-title">يتصل بكل <span>أدواتك.</span></h1>
      <p class="lead">متجرك أو CRM أو قنوات التواصل، كلها تعمل مع سوشل لاب بدون تعقيد.</p>
    </div>
  </section>
  <section class="int-list">
    <div class="wrap">
{groups}
      <div class="int-plans">
        <p><b>باقة الأعمال:</b> مفاتيح API · Odoo · n8n.</p>
        <p><b>الباقة المخصصة:</b> تكاملات مخصصة وحلول on-prem.</p>
        <a class="link-arrow" href="pricing.html">قارن الباقات</a>
      </div>
    </div>
  </section>
'''
    page('integrations.html', 'التكاملات | سوشل لاب', 'سوشل لاب يتصل بسلة وزد وشوبيفاي وWooCommerce وOdoo وZoho وSalesforce وHubSpot وGoogle وn8n وغيرها — 18 تكاملاً.', body, active='integrations')


# ---------------------------------------------------------------- case studies
def case_studies():
    body = f'''
  <section class="page-hero" aria-labelledby="page-title">
    <div class="wrap">
      <p class="eyebrow mono">دراسات الحالة</p>
      <h1 id="page-title" class="page-title">تجار تحقق <span>نتائج حقيقية.</span></h1>
      <p class="lead">من متاجر أزياء لسلاسل مطاعم، سوشل لاب يعمل لكل نوع عمل.</p>
    </div>
  </section>
  <section class="cases cases-page">
    <div class="wrap">
      {case_featured()}
      <div class="case-grid">
        {case_card('fashion')}
        {case_card('food')}
        {case_card('tech')}
      </div>
    </div>
  </section>
{stats_band()}
'''
    page('case-studies.html', 'دراسات الحالة | سوشل لاب', 'نتائج تجار يستخدمون سوشل لاب: 12 متجراً من لوحة واحدة، +240% مبيعات لمتجر أزياء، 98% رضا العملاء، و3x معدل التحويل.', body, active='cases')


# ---------------------------------------------------------------- pricing
def pricing():
    def card(p):
        price_y = f' data-yearly="{p["y"]}"' if p['y'] else ''
        usd_y = f' data-yearly="{p["usd_y"]}"' if p.get('usd_y') else ''
        alt = f'<p class="price-alt" data-alt>أو {p["y"]} ر.س / {p["usd_y"]} سنوياً</p>' if p['y'] else f'<p class="price-alt">{p["note"]}</p>'
        inc = f'<p class="inc">{p["inc"]}</p>' if p['inc'] else ''
        feats = '\n'.join(f'              <li>{icon("check")}{x}</li>' for x in p['feats'])
        quota = '\n'.join(f'              <li>{q}</li>' for q in p['quota'])
        badge = '<p class="badge">موصى به</p>' if p.get('pick') else ''
        cls = ' plan-pick' if p.get('pick') else ''
        return f'''          <li class="plan{cls}" id="plan-{p['key']}" role="tabpanel" aria-labelledby="tab-{p['key']}">
            {badge}
            <h3>{p['ar']} <span class="mono">{p['en']}</span></h3>
            <p class="plan-desc">{p['desc']}</p>
            <p class="price"><b class="mono" data-monthly="{p['m']}"{price_y}>{p['m']}</b><span>ر.س<br><em data-period>/ شهر</em></span><small class="mono" data-monthly="{p['usd']}"{usd_y}>{p['usd']}</small></p>
            {'<p class="vat">شامل الضريبة</p>' if p['y'] else '<p class="vat">&nbsp;</p>'}
            {alt}
            <a class="btn {'btn-lime' if p.get('pick') else 'btn-line'} btn-block" href="{p['cta'][1]}">{p['cta'][0]}</a>
            <ul class="quota">
{quota}
            </ul>
            {inc}
            <ul class="feats">
{feats}
            </ul>
          </li>'''

    tabs = '\n'.join(f'''        <button type="button" role="tab" id="tab-{p['key']}" aria-controls="plan-{p['key']}" aria-selected="{'true' if p.get('pick') else 'false'}" data-plan-tab="{p['key']}">{p['ar']}</button>''' for p in PLANS)
    cards = '\n'.join(card(p) for p in PLANS)
    e = ENTERPRISE
    rows = [('المستخدمون', 0), ('الرسائل شهرياً', 1), ('التخزين', 2), ('جهات الاتصال', 3)]
    table_rows = '\n'.join(
        '          <tr><th scope="row">' + label + '</th>' + ''.join(f'<td>{p["quota"][i]}</td>' for p in PLANS) + '<td>مخصص</td></tr>'
        for label, i in rows)
    body = f'''
  <section class="page-hero" aria-labelledby="page-title">
    <div class="wrap pricing-head">
      <div>
        <p class="eyebrow mono">الباقات والأسعار</p>
        <h1 id="page-title" class="page-title">باقات لكل مرحلة <span>من مراحل النمو.</span></h1>
        <p class="lead">من التجار الأفراد إلى فرق المؤسسات: ادفع مقابل ما تستخدمه فقط، وتوسّع بثقة.</p>
      </div>
      <div class="billing" role="group" aria-label="مدة الاشتراك">
        <button type="button" class="on" aria-pressed="true" data-billing="monthly">الاشتراك الشهري</button>
        <button type="button" aria-pressed="false" data-billing="yearly">الاشتراك السنوي <em>شهران مجاناً</em></button>
      </div>
    </div>
  </section>

  <section class="plans" aria-label="الباقات">
    <div class="wrap">
      <div class="plan-tabs" role="tablist" aria-label="اختر الباقة">
{tabs}
      </div>
      <div class="stairs">
        <svg class="stairs-line" viewBox="0 0 1000 300" preserveAspectRatio="none" aria-hidden="true">
          <path class="draw" d="M0 290 C 380 270, 720 200, 960 20" fill="none" stroke="url(#swoosh-fade)" stroke-width="6" stroke-linecap="round"/>
        </svg>
        <ol class="plan-list">
{cards}
        </ol>
      </div>

      <div class="enterprise">
        <div>
          <h3>{e['ar']} <span class="mono">{e['en']}</span></h3>
          <p class="plan-desc">{e['desc']} حسب الطلب — تسعير عبر عرض سعر.</p>
        </div>
        <ul class="feats">
{chr(10).join(f'          <li>{icon("check")}{x}</li>' for x in e['quota'] + e['feats'])}
        </ul>
        <a class="btn btn-line" href="{LINKS['calendly']}" target="_blank" rel="noopener">تواصل مع المبيعات</a>
      </div>

      <div class="compare">
        <h2 class="h3">مقارنة سريعة</h2>
        <div class="table-wrap" tabindex="0" role="region" aria-label="جدول مقارنة الباقات">
          <table>
            <thead><tr><th scope="col"></th>{''.join(f'<th scope="col">{p["ar"]}</th>' for p in PLANS)}<th scope="col">مخصص</th></tr></thead>
            <tbody>
{table_rows}
            </tbody>
          </table>
        </div>
        <p class="plans-note">الأسعار شاملة ضريبة القيمة المضافة. الاشتراك السنوي يعطيك شهرين مجاناً.</p>
      </div>
    </div>
  </section>
'''
    page('pricing.html', 'الباقات والأسعار | سوشل لاب', 'باقات سوشل لاب: مجاني للأبد، البداية 90.85 ر.س، النمو 286.35 ر.س، الأعمال 688.85 ر.س شهرياً، ومخصص للمؤسسات. شهران مجاناً بالاشتراك السنوي.', body, active='pricing')


# ---------------------------------------------------------------- demo
def demo():
    body = f'''
  <section class="page-hero" aria-labelledby="page-title">
    <div class="wrap">
      <p class="eyebrow mono">جرّب سوشل لاب</p>
      <h1 id="page-title" class="page-title">شاهده يعمل <span>على متجرك.</span></h1>
      <p class="lead">جرّب الآن كيف يرد سوشل لاب على عملائك، أو اطلب وكيلاً مدرّباً على متجرك أنت.</p>
      <nav class="demo-jump" aria-label="خيارات التجربة">
        <a href="#sim"><span class="mono">01</span> جرّب الآن</a>
        <a href="#own"><span class="mono">02</span> وكيل مدرّب على متجرك</a>
        <a href="#session"><span class="mono">03</span> جلسة مع الفريق</a>
      </nav>
    </div>
  </section>

  <!-- 1. Interactive simulator -->
  <section class="sim" id="sim" aria-labelledby="sim-title">
    <div class="wrap sim-grid">
      <div class="sim-copy">
        <p class="eyebrow mono">01 · جرّب الآن</p>
        <h2 id="sim-title" class="h2">اختر موقفاً <span>وشاهد الرد.</span></h2>
        <div class="sim-tabs" role="tablist" aria-label="المواقف">
          <button type="button" role="tab" aria-selected="true" data-scenario="product">{icon('ai')}<span><strong>عميل يسأل عن منتج</strong><small>وكيل الذكاء الاصطناعي</small></span></button>
          <button type="button" role="tab" aria-selected="false" data-scenario="cart">{icon('orders')}<span><strong>سلة متروكة</strong><small>تذكير على واتساب</small></span></button>
          <button type="button" role="tab" aria-selected="false" data-scenario="cod">{icon('call')}<span><strong>تأكيد الدفع عند الاستلام</strong><small>وكيل المكالمات الذكي</small></span></button>
          <button type="button" role="tab" aria-selected="false" data-scenario="comment">{icon('automation')}<span><strong>تعليق على إنستقرام</strong><small>الردود الذكية على التعليقات</small></span></button>
        </div>
        <p class="sim-note">مثال توضيحي لطريقة عمل المنصة.</p>
      </div>
      <div class="phone-stage">
        <div class="phone">
          <div class="phone-top">
            <img src="assets/img/mark.png" alt="" width="36" height="36">
            <div><strong data-sim-name>متجرك</strong><span class="status"><b class="dot"></b> <span data-sim-status>يرد تلقائياً</span></span></div>
            <span class="chip mono" data-sim-channel>واتساب</span>
          </div>
          <div class="chat sim-chat" id="sim-chat" aria-live="polite"></div>
          <button class="sim-replay" type="button" data-sim-replay>إعادة التشغيل</button>
        </div>
      </div>
    </div>
  </section>

  <!-- 2. Agent trained on the visitor's store -->
  <section class="own" id="own" aria-labelledby="own-title">
    <div class="wrap own-grid">
      <div>
        <p class="eyebrow mono">02 · وكيل مدرّب على متجرك</p>
        <h2 id="own-title" class="h2">جرّب الوكيل <span>على منتجاتك أنت.</span></h2>
        <ol class="own-steps">
          <li><span class="mono">1</span><div><strong>أرسل رابط متجرك</strong><p>من النموذج هنا، على واتساب.</p></div></li>
          <li><span class="mono">2</span><div><strong>نجهّز وكيلاً لمتجرك</strong><p>فريقنا يدرّب وكيل الذكاء الاصطناعي على منتجات متجرك.</p></div></li>
          <li><span class="mono">3</span><div><strong>جرّبه بنفسك</strong><p>يصلك رابط واتساب تسأل فيه الوكيل عن منتجاتك وتشوف ردوده.</p></div></li>
        </ol>
      </div>
      <form class="demo-form card-form" id="demo-form" novalidate>
        <div class="field"><label for="f-name">الاسم</label><input id="f-name" name="name" type="text" autocomplete="name" required></div>
        <div class="field"><label for="f-store">اسم المتجر</label><input id="f-store" name="store" type="text" required></div>
        <div class="field field-wide"><label for="f-url">رابط المتجر</label><input id="f-url" name="url" type="url" inputmode="url" placeholder="https://" dir="ltr" required></div>
        <div class="field"><label for="f-platform">منصة المتجر</label>
          <select id="f-platform" name="platform"><option>سلة</option><option>زد</option><option>شوبيفاي</option><option>WooCommerce</option><option>أخرى</option></select>
        </div>
        <div class="field"><label for="f-phone">رقم الجوال (واتساب)</label><input id="f-phone" name="phone" type="tel" inputmode="tel" autocomplete="tel" placeholder="05XXXXXXXX" dir="ltr" required></div>
        <p class="form-error" id="form-error" role="alert" hidden>أكمل الاسم واسم المتجر ورابطه ورقم الجوال.</p>
        <button class="btn btn-lime btn-block" type="submit">أرسل الطلب عبر واتساب {ARROW}</button>
        <p class="form-note">سيفتح واتساب برسالة جاهزة فيها بياناتك إلى فريق سوشل لاب، وترسلها أنت.</p>
      </form>
    </div>
  </section>

  <!-- 3. Live session -->
  <section class="session" id="session" aria-labelledby="session-title">
    <div class="wrap">
      <div class="bubble bubble-cta">
        <svg class="bubble-arrow" viewBox="0 0 300 300" aria-hidden="true">
          <path class="draw" d="M0 300 C 110 270, 200 190, 238 52" fill="none" stroke="#D9F27E" stroke-width="16" stroke-linecap="round"/>
          <path class="draw draw-late" d="M205 78 L240 40 L276 108" fill="none" stroke="#D9F27E" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        <div>
          <p class="eyebrow mono">03 · جلسة مع الفريق</p>
          <h2 id="session-title" class="h2">تفضّل تشوفه <span>مع فريقنا؟</span></h2>
          <p class="body">احجز جلستك المجانية الآن ونبني لك النظام خطوة بخطوة.</p>
        </div>
        <div class="cta-actions">
          <a class="btn btn-lime" href="{LINKS['calendly']}" target="_blank" rel="noopener">احجز جلسة مجانية {ARROW}</a>
          <a class="btn btn-line" href="{LINKS['wa']}" target="_blank" rel="noopener">راسلنا على واتساب</a>
          <p class="cta-note">بدون بطاقة ائتمان • إعداد في 10 دقائق</p>
        </div>
      </div>
    </div>
  </section>
'''
    page('demo.html', 'جرّب سوشل لاب على متجرك | سوشل لاب', 'جرّب الآن كيف يرد سوشل لاب على عملائك، أو اطلب وكيل ذكاء اصطناعي مدرّباً على متجرك، أو احجز جلسة مجانية مع الفريق.', body, active='demo', cta=False)


# ---------------------------------------------------------------- faq
def faq():
    items = '\n'.join(f'''        <details>
          <summary>{q}</summary>
          <p>{a}</p>
        </details>''' for q, a in FAQ)
    body = f'''
  <section class="page-hero" aria-labelledby="page-title">
    <div class="wrap">
      <p class="eyebrow mono">الأسئلة الشائعة</p>
      <h1 id="page-title" class="page-title">أسئلة <span>تتكرر.</span></h1>
      <p class="lead">لم تجد الإجابة التي تبحث عنها؟ تحدث مع فريقنا، أو تصفح <a class="inline-link" href="{LINKS['help']}">مركز المعرفة</a>.</p>
    </div>
  </section>
  <section class="faq">
    <div class="wrap faq-grid">
      <div class="faq-side">
        <a class="btn btn-line" href="{LINKS['wa']}" target="_blank" rel="noopener">تحدث معنا على واتساب</a>
      </div>
      <div class="faq-list">
{items}
      </div>
    </div>
  </section>
'''
    page('faq.html', 'الأسئلة الشائعة | سوشل لاب', 'إجابات عن سوشل لاب: كيف يعمل، علاقته بالتجارة الإلكترونية، ربط واتساب، الباقات، والتطبيق.', body, active='faq')


if __name__ == '__main__':
    home()
    for f in FEATURES:
        feature_page(f)
    integrations()
    case_studies()
    pricing()
    demo()
    faq()
