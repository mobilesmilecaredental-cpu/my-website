# Mobile Smile Care: Dental Hygiene — website

Plain static HTML, served by GitHub Pages from the `main` branch at
www.mobilesmilecare.ca (Cloudflare in front). No server code.

## What's here

    index.html                 Home
    children.html              Children
    busy-professionals.html    At home or at work
    seniors-mobility.html      Seniors & limited mobility
    care-homes.html            Long-term care & retirement homes
    insurance.html             Insurance & direct billing
    meet-lisa.html             Meet Lisa
    patient-forms.html         How intake forms work (forms come via Akitu)
    styles.css, site.js        Shared look and small enhancements
    fonts/, img/               Self-hosted fonts and web-optimized images
    sitemap.xml, robots.txt    For search engines
    CNAME                      Holds the domain. Do not delete.

    _build/                    Page sources + generator (not published)
    _photos/                   Original photos (not published)

## Editing pages

Page bodies live in _build/pages/<page>.html. Shared header, footer, contact
block, page titles/descriptions and Google structured data live in
_build/build.py. After editing, run:

    python _build/build.py

That rewrites the .html files at the top level. Commit those.

## Booking link

Book buttons currently point to the contact section. When the Akitu One
booking link is ready, set BOOK_HREF in _build/build.py and rebuild.

## Contact form

Sends through Web3Forms to mobilesmilecaredental@gmail.com
(key in _build/build.py). For general questions only; no health details.
