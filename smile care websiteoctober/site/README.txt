# Smile Care — website files

Everything in this folder is the complete website: plain HTML, no build
step, no installs, no server code. Upload the folder contents as-is.

## What's here

    index.html               Home page  (must keep this exact name)
    children.html            Children
    busy-professionals.html  Busy professionals
    seniors-mobility.html    Seniors & mobility
    care-homes.html          Long-term care & retirement homes
    insurance.html           Insurance & direct billing
    patient-forms.html       Patient intake forms
    site.js                  Menus, FAQ, forms, animations — keep it
    assets/                  Logo, QR code, images
    robots.txt               Tells search engines to index the site
    sitemap.xml              Lists all seven pages for search engines

Every page is finished HTML on its own — the text and layout are in the
file, so pages appear instantly and search engines read them directly.
site.js only adds the interactive extras (mobile menu, FAQ accordion,
form sending, scroll animations). If it were removed, the pages would
still read correctly; they just wouldn't be interactive.

## Publishing on GitHub Pages

1. Upload the CONTENTS of this folder to the root of your repo —
   index.html must sit at the top level, not inside a folder.
2. Settings → Pages → Deploy from a branch → main → / (root) → Save.
3. Do NOT delete the CNAME file GitHub added; it holds your domain.

## Turn on the inquiry forms (2 minutes)

Out of the box the forms open the visitor's own email app. To have
submissions land in your inbox automatically:

1. Go to https://web3forms.com
2. Enter mobilesmilecaredental@gmail.com and submit
3. They email you an access key (looks like a1b2c3d4-e5f6-...)
4. Open each .html file in a text editor and find, near the top:

       window.SMILE_CARE_FORM_KEY = "";

5. Paste your key between the quotes and save:

       window.SMILE_CARE_FORM_KEY = "a1b2c3d4-e5f6-...";

Do this in all seven files. Free tier covers 250 submissions/month.

## Domain & search

The live domain is https://www.mobilesmilecare.ca/ — it appears in the
canonical tags, sitemap.xml, and robots.txt. If it ever changes, ask me
to swap it and I'll regenerate the files.

Submit sitemap.xml in Google Search Console
(search.google.com/search-console) so the site gets indexed faster.

Most important step for local search: a free Google Business Profile
for Smile Care with the service area set to Windsor / Essex County.
Without it the practice won't appear in map results.

## Making changes later

Text and colours are plain HTML inside each file, editable in any text
editor. To swap an image, replace the file in assets/ keeping the same
filename, then re-upload.

## Notes

- Test on a real phone before sharing the link widely.
- Keep a copy of this folder somewhere safe as your master version.
