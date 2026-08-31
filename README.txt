# Smile Care — website files

Everything in this folder is the complete website. No build step, no
installs, no server code. Upload the folder as-is.

## What's here

    index.html          Home page  (must keep this exact name)
    care-homes.html     Long-term care & retirement homes
    insurance.html      Insurance & direct billing
    patient-forms.html  Patient intake forms
    support.js          Required — do not delete or rename
    assets/             Logo, QR code, images

Yes — index.html is required. Both GitHub Pages and Netlify serve
index.html automatically when someone visits your domain. The other
pages are reached by their filename (yoursite.com/insurance.html).

## Publishing on GitHub Pages

1. Create a new repository on github.com (public).
2. Upload the CONTENTS of this folder to the root of the repo —
   index.html must sit at the top level, not inside a "site" folder.
3. Repo → Settings → Pages → Source: "Deploy from a branch",
   Branch: main, Folder: / (root) → Save.
4. Wait ~1 minute. Your site is at
   https://<username>.github.io/<repo-name>/
5. Custom domain: Settings → Pages → Custom domain, then add the
   DNS records GitHub shows you at your registrar.

(Netlify alternative: drag this folder onto app.netlify.com/drop.)

## Before you publish: turn on the inquiry forms (2 minutes)

Out of the box the forms open the visitor's own email app. To have
submissions land in your inbox automatically:

1. Go to https://web3forms.com
2. Enter mobilesmilecaredental@gmail.com and submit
3. They email you an access key (looks like a1b2c3d4-e5f6-...)
4. Open each .html file in a text editor and find, near the top:

       window.SMILE_CARE_FORM_KEY = "";

5. Paste your key between the quotes and save:

       window.SMILE_CARE_FORM_KEY = "a1b2c3d4-e5f6-...";

Do this in all four files. Free tier covers 250 submissions/month.

## Making changes later

Text and colours are plain HTML inside each file, editable in any
text editor. To swap an image, replace the file in assets/ keeping
the same filename, then re-upload.

## Notes

- Test on a real phone before sharing the link widely.
- Keep a copy of this folder somewhere safe as your master version.
