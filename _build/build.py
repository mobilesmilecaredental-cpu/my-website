"""Assemble the site's static pages from _build/pages/*.html.

Shared header, footer, contact block and structured data live here so every
page stays consistent. Output is plain HTML at the repo root (what GitHub Pages
serves). Run:  python _build/build.py
Folders starting with "_" are not published by GitHub Pages.
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://www.mobilesmilecare.ca/"
PHONE_TEL = "+19059417580"
PHONE = "(905) 941-7580"
EMAIL = "mobilesmilecaredental@gmail.com"
NAME = "Mobile Smile Care: Dental Hygiene"
BOOK_HREF = "#contact"  # swap for the Akitu One booking link when it exists
FORM_KEY = "c8442fae-15a3-4455-824e-184189a23934"

TOWNS = ["Windsor", "LaSalle", "Tecumseh", "Amherstburg", "Lakeshore", "Belle River",
         "Essex", "Kingsville", "Leamington", "Harrow", "McGregor", "Comber"]

BUSINESS = {
    "@type": "MedicalBusiness",
    "@id": SITE + "#business",
    "name": NAME,
    "alternateName": "Mobile Smile Care",
    "description": ("Mobile dental hygiene practice. A Registered Dental Hygienist provides cleanings and "
                    "preventive dental hygiene care at home, at work, and in long-term care and retirement "
                    "homes across Windsor and Essex County, Ontario."),
    "url": SITE,
    "telephone": "+1-905-941-7580",
    "email": EMAIL,
    "logo": SITE + "img/logo-720.webp",
    "image": [SITE + "img/og-image.jpg", SITE + "img/lisa-hero-1200.webp"],
    "medicalSpecialty": "Dentistry",
    "knowsLanguage": ["en", "ro"],
    "address": {"@type": "PostalAddress", "addressLocality": "Windsor", "addressRegion": "ON", "addressCountry": "CA"},
    "areaServed": [{"@type": "City", "name": t} for t in TOWNS]
                  + [{"@type": "AdministrativeArea", "name": "Essex County, Ontario"}],
    "openingHoursSpecification": [
        {"@type": "OpeningHoursSpecification", "dayOfWeek": "Friday", "opens": "18:00", "closes": "21:00"},
        {"@type": "OpeningHoursSpecification", "dayOfWeek": "Saturday", "opens": "10:00", "closes": "20:00"},
        {"@type": "OpeningHoursSpecification", "dayOfWeek": "Sunday", "opens": "10:00", "closes": "18:00"},
    ],
    "paymentAccepted": "Direct billing to insurance, Canadian Dental Care Plan (CDCP), NIHB, ODSP",
    "availableService": [{"@type": "MedicalProcedure", "name": n} for n in [
        "Dental cleaning (scaling and polishing)", "Oral hygiene assessment and home-care coaching",
        "Fluoride varnish", "Pit and fissure sealants", "Oral cancer screening",
        "Silver diamine fluoride", "Interim stabilization therapy"]],
    "employee": {"@id": SITE + "#lisa"},
    "sameAs": ["https://www.instagram.com/mobile.smilecare/", "https://www.facebook.com/mobilesmilecaredentalhygiene/"],
}

LISA = {
    "@type": "Person",
    "@id": SITE + "#lisa",
    "name": "Lisa Suciu",
    "jobTitle": "Registered Dental Hygienist",
    "alumniOf": {"@type": "CollegeOrUniversity", "name": "Niagara College"},
    "knowsLanguage": ["en", "ro"],
    "worksFor": {"@id": SITE + "#business"},
    "image": SITE + "img/lisa-portrait-800.webp",
    "url": SITE + "meet-lisa.html",
}

HOME_FAQ = [
    ("What do I need for a home visit?", "Very little: a comfortable place to sit or recline, an electrical outlet and a nearby sink. I bring all the equipment and follow strict infection-control protocols."),
    ("Is a mobile cleaning as thorough as one at a clinic?", "Yes. I use clinic-grade portable equipment and sterilized instruments, and every visit includes the same assessment, scaling and polishing you’d receive in a clinic."),
    ("Do you bill my insurance directly?", "Yes. Direct billing is available for most private plans, and for the Canadian Dental Care Plan (CDCP), NIHB and ODSP."),
    ("Am I eligible for the CDCP?", "The Canadian Dental Care Plan covers eligible Canadian residents who meet income requirements and don’t have access to private dental insurance. I’m happy to help you check your coverage."),
    ("Do you visit long-term care and retirement homes?", "Yes. I provide on-site care in long-term care homes, retirement residences, assisted living and memory care, with no resident transport."),
    ("Is there a travel fee?", "A small travel fee may apply depending on where you are. We’ll confirm it together when you book."),
]

AUDIENCE = [
    ("children.html", "Children", "Gentle first visits at home"),
    ("busy-professionals.html", "Busy professionals", "At home or at work"),
    ("seniors-mobility.html", "Seniors &amp; limited mobility", "Unhurried care at home"),
    ("care-homes.html", "Care homes", "On-site for residents"),
]

PAGES = [
    dict(slug="index", file="index.html", path="",
         title="Mobile Dental Hygienist in Windsor &amp; Essex | Mobile Smile Care",
         description="Lisa Suciu, RDH, brings dental cleanings and preventive care to your home, workplace or care home across Windsor &amp; Essex County. Direct billing, CDCP accepted.",
         og_title="Mobile dental hygiene, brought to your door | Windsor &amp; Essex",
         preload_hero="lisa-hero", form_for="Myself", faq=HOME_FAQ),
    dict(slug="children", file="children.html", path="children.html", crumb="Children",
         title="Children’s Dental Cleanings at Home | Windsor &amp; Essex | Mobile Smile Care",
         description="Gentle dental hygiene visits for children at home in Windsor &amp; Essex: cleanings, fluoride, sealants and hands-on brushing practice, with no waiting room. CDCP and HSO billed directly.",
         og_title="Children’s dental hygiene at home | Windsor &amp; Essex",
         service="Mobile dental hygiene for children", form_for="My child"),
    dict(slug="busy-professionals", file="busy-professionals.html", path="busy-professionals.html", crumb="Busy professionals",
         title="Dental Cleanings at Home or at Work | Windsor &amp; Essex | Mobile Smile Care",
         description="A full dental hygiene appointment at your home or workplace in Windsor &amp; Essex: assessment, scaling and polishing with no commute and no waiting room. Direct billing.",
         og_title="Dental cleanings at home or at work | Windsor &amp; Essex",
         service="Mobile dental hygiene at home or at work", form_for="Myself"),
    dict(slug="seniors-mobility", file="seniors-mobility.html", path="seniors-mobility.html", crumb="Seniors &amp; limited mobility",
         title="Dental Hygiene at Home for Seniors &amp; Limited Mobility | Windsor &amp; Essex",
         description="Unhurried, dementia-informed dental hygiene at home for seniors and anyone with limited mobility in Windsor &amp; Essex County. Direct billing, CDCP accepted.",
         og_title="Gentle dental hygiene at home for seniors | Windsor &amp; Essex",
         service="Mobile dental hygiene for seniors and people with limited mobility", form_for="A parent or senior"),
    dict(slug="care-homes", file="care-homes.html", path="care-homes.html", crumb="Care homes",
         title="On-Site Dental Hygiene for Long-Term Care &amp; Retirement Homes | Windsor &amp; Essex",
         description="On-site dental hygiene for residents of long-term care and retirement homes in Windsor &amp; Essex County. No resident transport, no cost to your facility, notes after every visit.",
         og_title="On-site dental hygiene for care homes | Windsor &amp; Essex",
         service="On-site dental hygiene for long-term care and retirement homes", form_for="A care home"),
    dict(slug="insurance", file="insurance.html", path="insurance.html", crumb="Insurance &amp; billing",
         title="Insurance &amp; Direct Billing: CDCP, NIHB, ODSP | Mobile Smile Care",
         description="How direct billing works for mobile dental hygiene in Windsor &amp; Essex: private plans, the Canadian Dental Care Plan (CDCP), NIHB, ODSP and Healthy Smiles Ontario.",
         og_title="Insurance &amp; direct billing | Mobile Smile Care", form_for="Not sure yet"),
    dict(slug="meet-lisa", file="meet-lisa.html", path="meet-lisa.html", crumb="Meet Lisa",
         title="Meet Lisa Suciu, RDH | Mobile Dental Hygienist in Windsor",
         description="Lisa Suciu is a Registered Dental Hygienist and Niagara College graduate with 7 years of experience, providing mobile dental hygiene in English and Romanian across Windsor &amp; Essex.",
         og_title="Meet Lisa Suciu, Registered Dental Hygienist", profile=True, form_for="Myself"),
    dict(slug="patient-forms", file="patient-forms.html", path="patient-forms.html", crumb="Patient forms",
         title="Patient Forms | Mobile Smile Care: Dental Hygiene",
         description="How intake and medical history forms work for your mobile dental hygiene visit with Mobile Smile Care in Windsor &amp; Essex.",
         og_title="Patient forms | Mobile Smile Care", form_for="Myself"),
]

SPRITE = """<svg width="0" height="0" style="position:absolute" aria-hidden="true">
  <symbol id="i-phone" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" d="M5 4h3.2l1.6 4-2 1.3a10.5 10.5 0 0 0 6.9 6.9l1.3-2 4 1.6V19a1.8 1.8 0 0 1-1.9 1.8C10.4 20.3 3.7 13.6 3.2 5.9A1.8 1.8 0 0 1 5 4z"/></symbol>
  <symbol id="i-arrow" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" d="M4 12h15m-6-6 6 6-6 6"/></symbol>
  <symbol id="i-chev" viewBox="0 0 12 12"><path fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" d="m2.5 4.5 3.5 3.5 3.5-3.5"/></symbol>
  <symbol id="i-plus" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" d="M12 5v14M5 12h14"/></symbol>
  <symbol id="i-menu" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" d="M4 7h16M4 12h16M4 17h16"/></symbol>
  <symbol id="i-close" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" d="m6 6 12 12M18 6 6 18"/></symbol>
  <symbol id="i-cal" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="3.5" y="5" width="17" height="15" rx="1.5"/><path d="M3.5 10h17M8 3v4M16 3v4"/></g></symbol>
  <symbol id="i-check" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" d="m5 12.5 4.5 4.5L19 7.5"/></symbol>
  <symbol id="i-ig" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3.5" y="3.5" width="17" height="17" rx="4.5"/><circle cx="12" cy="12" r="4"/><circle cx="17.2" cy="6.8" r=".6" fill="currentColor"/></g></symbol>
  <symbol id="i-fb" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round" d="M14 20.5v-7h2.6l.4-3H14V8.7c0-.9.3-1.6 1.6-1.6h1.5V4.4a19 19 0 0 0-2.3-.1c-2.3 0-3.8 1.4-3.8 3.9v2.3H8.5v3H11v7"/></symbol>
</svg>"""


def arrow(size=None):
    dims = f' width="{size}" height="{size}"' if size else ""
    return f'<svg{dims} aria-hidden="true"><use href="#i-arrow"/></svg>'


def header(p):
    cur = p["file"]

    def aria(f):
        return ' aria-current="page"' if f == cur else ""
    menu_items = "\n".join(
        f'          <li><a href="{f}"{aria(f)}>{label}<small>{sub}</small></a></li>' for f, label, sub in AUDIENCE)
    sheet_items = "\n".join(
        f'          <a href="{f}"{aria(f)}>{label} {arrow(22)}</a>' for f, label, _ in AUDIENCE)
    return f"""<header class="site-header" id="top">
  <div class="wrap header-row">
    <a class="brand" href="index.html" aria-label="{NAME}, home">
      <img src="img/mark-96.png" width="30" height="33" alt="">
      <span class="brand-name"><b>Mobile Smile Care</b><span>Dental Hygiene</span></span>
    </a>
    <nav class="nav" aria-label="Main">
      <details class="navmenu">
        <summary>Who I help <svg aria-hidden="true"><use href="#i-chev"/></svg></summary>
        <ul>
{menu_items}
        </ul>
      </details>
      <a href="index.html#services">Services</a>
      <a href="insurance.html"{aria("insurance.html")}>Insurance</a>
      <a href="meet-lisa.html"{aria("meet-lisa.html")}>Meet Lisa</a>
      <a href="index.html#faq">FAQ</a>
    </nav>
    <div class="header-actions">
      <a class="tel tel-text" href="tel:{PHONE_TEL}"><svg aria-hidden="true"><use href="#i-phone"/></svg>{PHONE}</a>
      <a class="icon-btn" href="tel:{PHONE_TEL}" aria-label="Call {PHONE}"><svg aria-hidden="true"><use href="#i-phone"/></svg></a>
      <a class="btn btn--dark" href="{BOOK_HREF}" data-book>Book a visit</a>
      <details class="menu-toggle">
        <summary class="icon-btn" aria-label="Menu"><svg class="i-open" aria-hidden="true"><use href="#i-menu"/></svg><svg class="i-close" aria-hidden="true"><use href="#i-close"/></svg></summary>
        <nav class="menu-sheet" aria-label="Mobile">
          <span class="caps">Who I help</span>
{sheet_items}
          <span class="caps">More</span>
          <a href="index.html#services">Services</a>
          <a href="insurance.html"{aria("insurance.html")}>Insurance &amp; billing</a>
          <a href="meet-lisa.html"{aria("meet-lisa.html")}>Meet Lisa</a>
          <a href="patient-forms.html"{aria("patient-forms.html")}>Patient forms</a>
          <a href="index.html#faq">FAQ</a>
          <a class="btn btn--dark" href="{BOOK_HREF}" data-book>Book a visit</a>
        </nav>
      </details>
    </div>
  </div>
</header>"""


def contact(p):
    opts = ["Myself", "My child", "A parent or senior", "A care home", "Not sure yet"]
    options = "".join(
        f'<option{" selected" if o == p.get("form_for") else ""}>{o}</option>' for o in opts)
    care = p["slug"] == "care-homes"
    heading = "Talk about your residents" if care else "Book your visit"
    lede = ("Call, or send a note about your home and I’ll reply with availability and how a first visit could work."
            if care else "Call or text, or send a question and I’ll reply personally.")
    form_title = "Tell me about your home" if care else "Ask a question"
    note = ("Please share general details only: the number of residents and the kind of support you’re looking for."
            if care else "For booking questions, coverage or care-home inquiries. Please don’t include medical details here.")
    return f"""  <section class="section" id="contact" aria-labelledby="contact-title">
    <div class="wrap contact-grid">
      <div>
        <img class="contact-logo" src="img/logo-720.webp" width="720" height="720" alt="{NAME} logo" loading="lazy" decoding="async">
        <h2 id="contact-title">{heading}</h2>
        <p class="lede" style="margin-top:18px">{lede}</p>
        <ul class="contact-lines">
          <li><span class="caps">Phone</span><a href="tel:{PHONE_TEL}">{PHONE}</a></li>
          <li><span class="caps">Email</span><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><span class="caps">Hours</span>
            <dl class="hours"><dt>Friday</dt><dd>6 – 9 pm</dd><dt>Saturday</dt><dd>10 am – 8 pm</dd><dt>Sunday</dt><dd>10 am – 6 pm</dd></dl>
          </li>
        </ul>
      </div>
      <form class="form-card" data-form novalidate>
        <h3>{form_title}</h3>
        <p class="note">{note}</p>
        <input type="hidden" name="subject" value="New {'care-home inquiry' if care else 'question'} from mobilesmilecare.ca">
        <input class="hp" type="checkbox" name="botcheck" tabindex="-1" autocomplete="off" aria-hidden="true">
        <div class="field-row">
          <div class="field"><label for="f-name">Your name</label><input id="f-name" name="name" autocomplete="name" required></div>
          <div class="field"><label for="f-phone">Phone <span>(optional)</span></label><input id="f-phone" name="phone" type="tel" autocomplete="tel" inputmode="tel"></div>
        </div>
        <div class="field"><label for="f-email">Email</label><input id="f-email" name="email" type="email" autocomplete="email" required></div>
        <div class="field"><label for="f-for">The visit is for</label>
          <select id="f-for" name="visit_for">{options}</select>
        </div>
        <div class="field"><label for="f-msg">{'Your message' if care else 'Your question'}</label><textarea id="f-msg" name="message" required></textarea></div>
        <button class="btn btn--dark" type="submit">{'Send message' if care else 'Send question'}</button>
        <p class="form-status" role="status" aria-live="polite"></p>
      </form>
    </div>
  </section>"""


def footer():
    who = "\n".join(f'          <li><a href="{f}">{label}</a></li>' for f, label, _ in AUDIENCE)
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <img class="brand-mark" src="img/mark-96.png" width="34" height="37" alt="">
        <h2>{NAME}</h2>
        <p>Professional dental hygiene at home, at work and in care residences across Windsor &amp; Essex County.</p>
        <div class="socials">
          <a href="https://www.instagram.com/mobile.smilecare/" aria-label="Instagram" rel="noopener" target="_blank"><svg aria-hidden="true"><use href="#i-ig"/></svg></a>
          <a href="https://www.facebook.com/mobilesmilecaredentalhygiene/" aria-label="Facebook" rel="noopener" target="_blank"><svg aria-hidden="true"><use href="#i-fb"/></svg></a>
        </div>
      </div>
      <div>
        <p class="caps">Who I help</p>
        <ul>
{who}
        </ul>
      </div>
      <div>
        <p class="caps">The practice</p>
        <ul>
          <li><a href="meet-lisa.html">Meet Lisa</a></li>
          <li><a href="insurance.html">Insurance &amp; billing</a></li>
          <li><a href="patient-forms.html">Patient forms</a></li>
          <li><a href="index.html#faq">FAQ</a></li>
        </ul>
      </div>
      <div>
        <p class="caps">Contact</p>
        <ul>
          <li><a href="tel:{PHONE_TEL}">{PHONE}</a></li>
          <li><a href="mailto:{EMAIL}">Email Lisa</a></li>
        </ul>
        <dl class="hours" style="margin-top:16px"><dt>Fri</dt><dd>6 – 9 pm</dd><dt>Sat</dt><dd>10 am – 8 pm</dd><dt>Sun</dt><dd>10 am – 6 pm</dd></dl>
      </div>
    </div>
    <div class="legal"><span>© 2026 {NAME}</span><span>Lisa Suciu, Registered Dental Hygienist · Windsor, Ontario</span></div>
  </div>
</footer>

<div class="action-bar" aria-label="Quick actions">
  <a class="btn btn--line" href="tel:{PHONE_TEL}"><svg aria-hidden="true"><use href="#i-phone"/></svg>Call</a>
  <a class="btn btn--dark" href="{BOOK_HREF}" data-book><svg aria-hidden="true"><use href="#i-cal"/></svg>Book</a>
</div>"""


def plain(s):
    return s.replace("&amp;", "&")


def schema(p):
    url = SITE + p["path"]
    graph = [BUSINESS, LISA]
    page = {"@type": "ProfilePage" if p.get("profile") else "WebPage", "@id": url + "#webpage", "url": url,
            "name": plain(p["title"]), "description": plain(p["description"]), "inLanguage": "en-CA",
            "isPartOf": {"@id": SITE + "#website"}, "about": {"@id": SITE + "#business"}}
    if p.get("profile"):
        page["mainEntity"] = {"@id": SITE + "#lisa"}
    graph.append(page)
    if p["slug"] == "index":
        graph.append({"@type": "WebSite", "@id": SITE + "#website", "url": SITE, "name": NAME,
                      "publisher": {"@id": SITE + "#business"}, "inLanguage": "en-CA"})
    else:
        graph.append({"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE},
            {"@type": "ListItem", "position": 2, "name": plain(p["crumb"]), "item": url}]})
    if p.get("service"):
        graph.append({"@type": "Service", "name": p["service"], "serviceType": "Dental hygiene",
                      "provider": {"@id": SITE + "#business"}, "url": url,
                      "areaServed": {"@type": "AdministrativeArea", "name": "Windsor and Essex County, Ontario"}})
    if p.get("faq"):
        graph.append({"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faq"]]})
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1)


def head(p):
    url = SITE + p["path"]
    preload = ""
    if p.get("preload_hero"):
        n = p["preload_hero"]
        preload = (f'<link rel="preload" as="image" type="image/avif" imagesrcset="img/{n}-600.avif 600w, '
                   f'img/{n}-900.avif 900w, img/{n}-1200.avif 1200w" imagesizes="(max-width: 860px) 92vw, 500px" fetchpriority="high">\n')
    return f"""<!doctype html>
<html lang="en-CA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{p["title"]}</title>
<meta name="description" content="{p["description"]}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#F3F2F0">
<link rel="icon" href="img/icon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="img/icon-180.png">
<meta property="og:type" content="{'profile' if p.get('profile') else 'website'}">
<meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{p["og_title"]}">
<meta property="og:description" content="{p["description"]}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}img/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="en_CA">
<meta name="twitter:card" content="summary_large_image">
<link rel="preload" href="fonts/spectral-300-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="fonts/atkinson-hyperlegible-next-400-700-latin.woff2" as="font" type="font/woff2" crossorigin>
{preload}<link rel="stylesheet" href="styles.css">
<script>document.documentElement.classList.add('js')</script>
<script type="application/ld+json">
{schema(p)}
</script>
</head>"""


def crumbs(p):
    if p["slug"] == "index":
        return ""
    return f'<nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> / <span aria-current="page">{p["crumb"]}</span></nav>'


def build():
    for p in PAGES:
        body = open(os.path.join(ROOT, "_build", "pages", p["slug"] + ".html"), encoding="utf-8").read()
        body = body.replace("{{crumbs}}", crumbs(p)).replace("{{book}}", BOOK_HREF).replace("{{tel}}", PHONE_TEL).replace("{{phone}}", PHONE)
        html = "\n".join([
            head(p), "<body>", '<a class="skip" href="#main">Skip to content</a>', "", SPRITE, "", header(p), "",
            '<main id="main">', body.rstrip("\n"), "", contact(p), "", "</main>", "", footer(), "",
            f'<script>window.SMILE_CARE_FORM_KEY = "{FORM_KEY}";</script>',
            '<script src="site.js" defer></script>', "</body>", "</html>", ""])
        with open(os.path.join(ROOT, p["file"]), "w", encoding="utf-8", newline="\n") as f:
            f.write(html)
        print("built", p["file"], len(html))


if __name__ == "__main__":
    build()
