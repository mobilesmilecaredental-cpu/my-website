---
name: Mobile Smile Care
description: Calling-card stationery for a boutique house-call dental hygiene practice in Windsor and Essex.
colors:
  porcelain: "#F3F2F0"
  card-stock: "#FBFAF8"
  linen: "#E9E4DD"
  linen-deep: "#DED6CB"
  espresso: "#221A15"
  espresso-2: "#2E241E"
  espresso-hover: "#3A2D24"
  ink: "#2A211B"
  ink-soft: "#5B4E43"
  bronze: "#9A7449"
  bronze-text: "#76572F"
  foil: "#CDA977"
  foil-hover: "#DDBB89"
  halo: "#F6D9A8"
  on-dark: "#F1EBE3"
  on-dark-soft: "#CFC1B0"
  line: "#D3C9BC"
  line-dark: "#4A3D33"
  foil-line: "rgba(205,169,119,.78)"
  field-stroke: "#BFB3A4"
  error: "#A3402E"
typography:
  display:
    fontFamily: "Spectral, Georgia, 'Times New Roman', serif"
    fontSize: "clamp(2.6rem, 1.7rem + 3.6vw, 4.75rem)"
    fontWeight: 300
    lineHeight: 1.08
    letterSpacing: "-0.015em"
  display-inner:
    fontFamily: "Spectral, Georgia, 'Times New Roman', serif"
    fontSize: "clamp(2.4rem, 1.6rem + 2.8vw, 4rem)"
    fontWeight: 300
    lineHeight: 1.08
    letterSpacing: "-0.015em"
  headline:
    fontFamily: "Spectral, Georgia, 'Times New Roman', serif"
    fontSize: "clamp(2.05rem, 1.5rem + 2.2vw, 3.25rem)"
    fontWeight: 300
    lineHeight: 1.08
    letterSpacing: "-0.015em"
  router-title:
    fontFamily: "Spectral, Georgia, 'Times New Roman', serif"
    fontSize: "clamp(1.65rem, 1.3rem + 1.5vw, 2.5rem)"
    fontWeight: 300
    lineHeight: 1.1
  title:
    fontFamily: "Spectral, Georgia, 'Times New Roman', serif"
    fontSize: "clamp(1.3rem, 1.15rem + .5vw, 1.55rem)"
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: "-0.005em"
  term:
    fontFamily: "Spectral, Georgia, 'Times New Roman', serif"
    fontSize: "1.2rem"
    fontWeight: 500
    lineHeight: 1.3
  lede:
    fontFamily: "'Atkinson Hyperlegible Next', 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: "clamp(1.15rem, 1.05rem + .45vw, 1.35rem)"
    fontWeight: 400
    lineHeight: 1.6
  body:
    fontFamily: "'Atkinson Hyperlegible Next', 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: "clamp(1.0625rem, .98rem + .3vw, 1.1875rem)"
    fontWeight: 400
    lineHeight: 1.6
  button:
    fontFamily: "'Atkinson Hyperlegible Next', 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: "1rem"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "0.01em"
  label:
    fontFamily: "'Atkinson Hyperlegible Next', 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: ".8125rem"
    fontWeight: 700
    letterSpacing: "0.14em"
rounded:
  card: "3px"
  focus: "2px"
spacing:
  gutter: "clamp(20px, 4vw, 48px)"
  section: "clamp(72px, 10vw, 136px)"
  wrap: "1200px"
  row: "24px"
components:
  button-primary:
    backgroundColor: "{colors.espresso}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button}"
    rounded: "{rounded.card}"
    padding: ".8em 1.5em"
    height: "52px"
  button-primary-hover:
    backgroundColor: "{colors.espresso-hover}"
    textColor: "#FFFFFF"
  button-line:
    backgroundColor: "transparent"
    textColor: "{colors.espresso}"
    typography: "{typography.button}"
    rounded: "{rounded.card}"
    padding: ".8em 1.5em"
    height: "52px"
  button-foil:
    backgroundColor: "{colors.foil}"
    textColor: "{colors.espresso}"
    typography: "{typography.button}"
    rounded: "{rounded.card}"
    padding: ".8em 1.5em"
    height: "52px"
  button-foil-hover:
    backgroundColor: "{colors.foil-hover}"
    textColor: "{colors.espresso}"
  button-ghost-dark:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.button}"
    rounded: "{rounded.card}"
    padding: ".8em 1.5em"
    height: "52px"
  input-field:
    backgroundColor: "#FFFFFF"
    textColor: "{colors.ink}"
    rounded: "{rounded.card}"
    padding: "12px 14px"
    height: "52px"
  form-card:
    backgroundColor: "{colors.card-stock}"
    textColor: "{colors.ink}"
    rounded: "{rounded.card}"
    padding: "clamp(24px, 3.5vw, 40px)"
  town-tag:
    textColor: "{colors.ink}"
    rounded: "{rounded.card}"
    padding: "8px 16px"
  nav-link:
    textColor: "{colors.ink}"
    rounded: "{rounded.card}"
    padding: "0 12px"
    height: "44px"
---

# Design System: Mobile Smile Care

## Overview

**Creative North Star: "The Calling Card, Left at Your Door"**

The site reads as fine stationery from a boutique house-call practice. The ground is porcelain card stock, the same near-white the logo sits on, so the logo blends into the page rather than sitting in a box. Espresso ink, the colour of Lisa's scrubs, owns whole bands of the page. Bronze foil appears as hairlines, rules, numerals and the single warm halo arc taken from the logo. Nothing is loud; trust comes from real photographs, plain facts set in quiet ruled lists, and a phone number that is always one tap away.

Density is generous and editorial: wide section padding, two-column grids that collapse to one column at 860px, and content held to readable measures (36ch ledes, 62 to 68ch prose). Information is organised by hairline rules rather than boxes. Lists of steps, services, billing plans, facts and FAQ answers are all ruled rows on open stock, not cards. Boxed containers are reserved for the things you fill in or must notice (the contact form, a callout figure).

Motion is slow and settled (a long ease-out), never bouncy: the halo arc draws itself once, router rows slide and take a foil underline, arrows nudge. Every movement has a reduced-motion fallback.

**Key Characteristics:**
- Porcelain and linen stock, espresso bands, bronze foil hairlines.
- Light Spectral serif for display; Atkinson Hyperlegible Next for everything read or tapped.
- Hairline-ruled lists instead of card grids.
- Trimmed-card corners (3px) everywhere; no pills, no large radii.
- Soft, long, low shadows only under photographs and the primary button.
- One signature interaction: the audience router on the espresso band.

## Colors

A warm, low-chroma stationery palette: two paper stocks, one dark ink that also serves as the band colour, and bronze in three strengths tuned to where it sits.

### Primary
- **Espresso Ink** (espresso): the primary action colour ("Book a visit"), full-bleed dark bands (the router, CTA bands) and the footer. Headings on light stock use it as their ink. Hover deepens toward a lifted espresso (espresso-hover).
- **Espresso Hover Layer** (espresso-2): the faint lift that fills a router row on hover or focus.

### Secondary
- **Bronze Foil** (bronze): hairline accents on light stock: list dots, step numerals, the halo arc, focus outlines, select chevrons, input caret, icon tint. Never used for small text.
- **Bronze Text** (bronze-text): the AA-passing bronze for links, small-caps labels, the brand sub-line, plan abbreviations and the bilingual greeting on light stock.
- **Gold Foil** (foil): bronze as it reads on espresso: router arrows and links, footer column labels, dark-band focus outlines, the gold button, and the fading foil rule.
- **Foil Line** (foil-line): 78% gold foil for hairline rules inside espresso bands.

### Tertiary
- **Halo Glow** (halo): the logo's warm halo. Used only as the soft radial glow behind the hero portrait and as the text-selection colour.

### Neutral
- **Porcelain** (porcelain): the page ground and the sticky header / mobile action bar (at 94 to 96% opacity).
- **Card Stock** (card-stock): the brighter raised paper of the form card, callouts and the nav dropdown.
- **Linen** (linen): secondary stock for alternate bands and menu hover rows; also the scrollbar track.
- **Linen Deep** (linen-deep): the deeper linen reserved for stock contrast.
- **Ink** (ink): body text on light stock.
- **Ink Soft** (ink-soft): secondary copy, ledes, captions, list descriptions, breadcrumbs.
- **On Dark / On Dark Soft** (on-dark, on-dark-soft): headings and body copy inside espresso bands.
- **Rule** (line): the universal hairline on light stock; also the outline button and tag border.
- **Rule on Dark** (line-dark): hairlines and ghost-button borders inside espresso.
- **Field Stroke** (field-stroke): the slightly darker stroke for form inputs, so fields read as fillable.
- **Error Brick** (error): invalid-field border; the error status panel pairs a pale brick ground with deep brick text.

### Named Rules
**The Foil Is Not Ink Rule.** Raw bronze (bronze) is for rules, numerals, icons, arcs and large serif type only. Any bronze text at body or label size uses bronze-text on light stock or foil on espresso.

**The Logo Stock Rule.** The page ground stays porcelain so the logo (on its own #F2F2F1 ground) sits on the page seamlessly. Do not put the logo on linen, white or espresso.

**The Single Halo Rule.** The only gradient fills in the system are the warm halo glow behind the hero portrait and the fade at the ends of a foil rule. Surfaces, buttons and bands are flat colour.

## Typography

**Display Font:** Spectral (with Georgia, Times New Roman), self-hosted at weights 300 and 500.
**Body Font:** Atkinson Hyperlegible Next (with Segoe UI, system-ui), self-hosted variable 400 to 700.

**Character:** A sharp, light classical serif for headings, like engraved letterhead, paired with a sans built for low-vision legibility, because many readers are older or on a phone.

### Hierarchy
- **Display** (Spectral 300, clamp 2.6 to 4.75rem, 1.08, -0.015em): the home hero H1 only, held to about 15ch and balanced. On narrow screens it drops to clamp(2.1rem, 1.6rem + 2.6vw, 2.6rem) so the H1 and both actions fit in the first screen.
- **Display Inner** (Spectral 300, clamp 2.4 to 4rem): inner-page H1s, max 18ch.
- **Headline** (Spectral 300, clamp 2.05 to 3.25rem): section H2s. Inside prose columns it steps down to clamp(1.8rem, 1.4rem + 1.4vw, 2.5rem).
- **Router Title** (Spectral 300, clamp 1.65 to 2.5rem, 1.1): the large light row titles in the audience router.
- **Title** (Spectral 500, clamp 1.3 to 1.55rem, 1.2): H3s, step titles, card headings.
- **Term** (Spectral 500, about 1.15 to 1.22rem, 1.25 to 1.3): service names, plan names, fact values, FAQ questions (fluid up to 1.35rem), footer practice name. Serif-500 is how a fact is named.
- **Lede** (Atkinson 400, clamp 1.15 to 1.35rem, ink-soft): one-sentence intros under H1s, max 36ch (44ch on inner pages).
- **Body** (Atkinson 400, clamp 1.0625 to 1.1875rem, 1.6): all reading text, measure 62 to 68ch.
- **Button** (Atkinson 700, 1rem, 0.01em): buttons, the phone number, arrow links.
- **Label** (Atkinson 700, 0.8125rem, 0.14em, uppercase): small caps that name a fact or a group: definition terms (Trained, Experience, Languages), contact line names (Phone, Email, Hours), footer column heads, mobile-menu group heads, program jurisdictions. Usually bronze-text on light, foil on dark; shrinks to 0.72 to 0.75rem in the footer and contact lines.
- **Numerals** (Spectral 300, 2.4rem, bronze): the counter that numbers visit steps. The callout figure uses Spectral 300 at clamp(2.4rem, 1.8rem + 2.4vw, 3.6rem) in bronze-text.

### Named Rules
**The Light Serif Rule.** Display and section headings are Spectral at weight 300; weight 500 is reserved for titles and named facts. No bold display type.

**The Label Names a Fact Rule.** Small caps label data (a term, a contact line, a menu group, a footer column). They never sit above a heading as a decorative tagline or restate the heading below them.

**The Bilingual Line.** The Romanian greeting is set as a serif line in bronze-text (300 weight in the home "hello", 500 in the language note), marked with lang="ro". It is a typographic statement, not a badge.

## Layout

A single centred column of max 1200px plus fluid gutters (clamp 20 to 48px each side). Sections breathe with clamp(72px, 10vw, 136px) vertical padding; CTA bands use clamp(64px, 8vw, 104px).

Most sections are two-column asymmetric grids (1.08/0.92, 0.8/1.2, 1/1.15, 1.1/0.9) with column gaps of clamp(40px, 6vw, 96px). A section head is itself a two-column grid: heading left, short explanatory paragraph right (max 46ch), aligned to the baseline. Everything collapses to one column at 860px; on collapse, the hero portrait and inner-page photos move above the text and crop wider (2:1 hero, 5:4 inner).

Service lists use a three-column definition grid (two at 980px, one at 620px) with a 48px column gap and no row gap, separated by top hairlines. The footer is 1.4/1/1/1, then two columns at 900px, then one at 560px.

The header is sticky at 76px (68px under 1080px, where the nav becomes a full-screen porcelain sheet of serif links). Under 760px a fixed bottom action bar (call + book) slides up once the hero has scrolled past. Scroll padding is 96px so anchors clear the header.

Row rhythm inside ruled lists is 22 to 24px vertical padding; label-to-value gaps are 6 to 8px; buttons in a group sit 12px apart.

## Elevation & Depth

Depth comes from paper, not panels. Most of the page is flat stock separated by tone (porcelain, linen, espresso) and hairline rules. Shadows are soft, long and pulled in with a negative spread, so they read as a photo or card resting on paper rather than floating. There are no hard or offset shadows.

### Shadow Vocabulary
- **Print Rest** (`box-shadow: 0 30px 60px -36px rgba(34,26,21,.5)`): under photographs (Lisa, the visit photo, inner-page photos). The hero portrait uses a slightly stronger -32px / .45 variant.
- **Inset Print** (`box-shadow: 0 24px 48px -28px rgba(34,26,21,.55)`): the small overlapping photo in the visit composition, which also carries a 6px porcelain border like a mounted print.
- **Ink Press** (`box-shadow: 0 1px 0 rgba(255,255,255,.06) inset, 0 8px 18px -10px rgba(34,26,21,.55)`): the espresso primary button only.
- **Dropdown** (`box-shadow: 0 2px 4px rgba(34,26,21,.06), 0 16px 32px -12px rgba(34,26,21,.28)`): the desktop "Who I help" menu panel.
- **Field Focus** (`box-shadow: 0 0 0 3px rgba(154,116,73,.22)`): a soft bronze ring around focused inputs.

### Named Rules
**The Resting Print Rule.** Shadows belong to photographs, the primary button and floating menus. Ruled lists, bands, tags and the form card stay flat.

## Shapes

Corners are trimmed card: 3px on every button, photo, field, tag, callout, menu and form card; 2px on focus outlines. The only circles are the 5px bronze bullets in the credentials line. Edges are otherwise crisp. The recurring silhouettes are the hairline rule (1px, line or foil-line), the fading foil rule (transparent to foil to transparent), and the thin bronze halo arc drawn over the hero portrait. Photographs are cropped to fixed print ratios: 3:4 hero portrait, 4:5 profile and inset photos, 1:1 visit photo, 4:3 wide inner photos.

## Components

### Buttons
Confident, compact and plainly labelled, with an icon at 18px where it helps.
- **Shape:** trimmed card (3px), min height 52px (46px in the header, 50px in the mobile action bar), 1px border.
- **Primary (espresso):** espresso fill, on-dark text, Ink Press shadow. Hover lifts to espresso-hover with white text and a 1px rise.
- **Outline:** transparent with a line-coloured border and espresso text; hover turns the border bronze and adds a 50% white wash.
- **Gold foil:** for the primary action inside espresso bands; foil fill, espresso text, hover brightens to foil-hover with a 1px rise.
- **Ghost on dark:** transparent with a line-dark border and on-dark text; hover turns the border foil.
- **Press / disabled:** active scales to 0.985; disabled drops to 55% opacity with a wait cursor.
- **Transitions:** 0.25s on the shared long ease-out curve.

### Arrow Link
A bold text link with a 20px arrow that nudges 4px right on hover. bronze-text on light stock, foil on espresso. The standard "read more" path.

### Phone Link
Espresso, bold, tabular figures, with a bronze phone icon. Always present in the header on desktop and in the mobile action bar.

### Tags (service towns)
- **Style:** 1px line border, 3px corners, 35% white wash, 8px by 16px padding, 0.98rem text. Static, not interactive.

### Cards / Containers
- **Form card and callout:** card-stock ground, 1px line border, 3px corners, clamp(24 to 40px) or clamp(28 to 44px) padding, flat.
- **Ruled lists** (steps, services, plans, facts, contact lines, programs, FAQ): no container at all. Each row has a top hairline; the last row adds a bottom hairline. Inside espresso bands the rules switch to foil-line.

### Inputs / Fields
- **Style:** white fill, field-stroke 1px border, 3px corners, 12px by 14px padding, min height 52px, 1.05rem text, bronze caret. Labels are bold 0.95rem above the field with optional hints in regular ink-soft. Selects use a custom bronze chevron.
- **Focus:** border turns bronze plus a 3px bronze ring at 22%.
- **Error:** border turns error brick; the status panel is pale brick with deep brick text. Success uses a pale sage panel with deep green text.

### Navigation
- **Desktop:** Atkinson 500 at 0.98rem in ink, 44px tall targets. Hover and current page turn bronze-text; the current page also takes a bronze underline. "Who I help" is a details disclosure opening a card-stock dropdown (Dropdown shadow) of two-line links (name plus a small ink-soft description), with linen row hover.
- **Mobile (1080px and below):** a 48px outlined icon button opens a full-screen porcelain sheet of Spectral 300 links at 1.6rem, separated by hairlines, grouped under small-caps labels, ending in a full-width primary button.
- **Header:** porcelain at 94% with a light blur, borderless at the top of the page; a line hairline appears once the page scrolls.

### Audience Router (signature)
The "Who's the visit for?" list on an espresso band. Each row is a three-column grid (light serif title, on-dark-soft description, foil "go" label with a 22px arrow) between foil-line hairlines. On hover or focus the title and description slide 14px right, the row fills with espresso-2, the arrow moves 6px, and a gold foil underline sweeps in from the left over 0.6s. Reduced motion keeps the fill and drops the movement. On mobile the description wraps under the title and the go label shrinks to its arrow.

### Visit Steps
Numbered rows with a large light bronze serif numeral (2.4rem) in a 56px gutter, a serif title and ink-soft text. Numerals switch to foil inside espresso bands.

### Hero Portrait
A tall 3:4 photo of Lisa with 3px trimmed corners and Print Rest shadow, under a thin 1.2px bronze halo arc that draws itself once (1.8s) on load, with the warm halo glow behind it. Caption below in ink-soft with her name in bold espresso. Under 860px it moves first and crops to 2:1.

### Credentials Line
A wrapping row of short facts under a top hairline, each led by a 5px bronze dot, in ink-soft at 0.95rem.

### Checklist
Rows with a 22px bronze check icon (foil on espresso) beside the text, 14px apart.

## Do's and Don'ts

### Do:
- **Do** keep the page on porcelain and let espresso take whole bands, not small boxes.
- **Do** separate list content with 1px hairlines (line on light stock, foil-line on espresso) instead of boxing it into cards.
- **Do** use bronze-text for any bronze text at body or label size, and raw bronze only for rules, numerals, icons and arcs.
- **Do** keep every corner at 3px.
- **Do** set headings in Spectral 300 and reading text in Atkinson Hyperlegible Next at no less than about 1.06rem.
- **Do** give every motion a reduced-motion fallback and use the shared long ease-out curve.
- **Do** keep tap targets at least 44px (buttons 52px) and keep the phone number one tap away on every page.
- **Do** use real photographs cropped to the print ratios (3:4, 4:5, 1:1, 4:3) with the Print Rest shadow.

### Don't:
- **Don't** use gradient fills on surfaces, buttons or bands; the halo glow and the foil-rule fade are the only gradients.
- **Don't** use pill shapes or radii above 3px.
- **Don't** use hard or offset shadows, or put shadows on ruled lists, bands or tags.
- **Don't** put small-caps labels above headings as taglines; labels name facts.
- **Don't** set small text in raw bronze on porcelain; it fails contrast.
- **Don't** use translucent glass panels; the sticky header and action bar stay 94 to 96% opaque porcelain.
- **Don't** add a new accent hue; the palette is porcelain, linen, espresso and bronze.
