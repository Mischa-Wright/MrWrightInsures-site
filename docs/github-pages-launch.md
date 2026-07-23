# GitHub Pages Launch Checklist
mrwrightinsures.com — free hosting, no Tilda needed.

## What's already done
- site/ folder is the complete built website (20 pages, all images, CSS, JS)
- CNAME file contains "mrwrightinsures.com"
- .nojekyll file prevents Jekyll from mangling the files
- .github/workflows/deploy.yml auto-deploys on every push to main
- Forms are wired to POST to a data-endpoint attribute; see Formspree section below

---

## Step 1: Create a GitHub account (2 min)
Go to github.com → Sign up. Use an email you check regularly.
Username suggestion: mischa-wright-insurance (or similar — it won't appear on the site)

## Step 2: Create a new repository (2 min)
1. Click the + icon → "New repository"
2. Name it: mrwrightinsures-site (or anything you like)
3. Set it to PUBLIC (required for free GitHub Pages)
4. Do NOT add a README, .gitignore, or license — leave it empty
5. Click "Create repository"

## Step 3: Upload the site files (5 min — no coding required)
Option A — Browser upload (easiest):
1. On the new empty repo page, click "uploading an existing file"
2. Drag the ENTIRE CONTENTS of the website-v2 folder (not the folder itself — open it first, then select everything inside) into the upload area
3. This includes: site/, .github/, docs/, build/, README.md
4. Scroll down, add commit message "Initial site launch", click "Commit changes"

Option B — Git command line (faster if you're comfortable):
  git init
  git add .
  git commit -m "Initial site launch"
  git remote add origin https://github.com/YOUR-USERNAME/mrwrightinsures-site.git
  git push -u origin main

## Step 4: Enable GitHub Pages (2 min)
1. In the repository, click Settings → Pages (left sidebar)
2. Under "Source", select "GitHub Actions" (not "Deploy from a branch")
3. The deploy workflow runs automatically. Click "Actions" tab to watch it.
4. After ~60 seconds you'll see a green checkmark. The site is live at
   https://YOUR-USERNAME.github.io/mrwrightinsures-site

## Step 5: Add your custom domain (5 min + DNS wait)
1. Still in Settings → Pages, under "Custom domain" enter:
   mrwrightinsures.com
   Click Save. This creates/confirms the CNAME file.

2. Log into your domain registrar (wherever you bought mrwrightinsures.com)
   Add these DNS records:

   TYPE    NAME    VALUE
   A       @       185.199.108.153
   A       @       185.199.109.153
   A       @       185.199.110.153
   A       @       185.199.111.153
   CNAME   www     YOUR-USERNAME.github.io

   (Replace YOUR-USERNAME with your actual GitHub username)

3. Wait 15 min to a few hours for DNS to propagate.
4. Return to Settings → Pages → tick "Enforce HTTPS". Done.

The site is now live at https://mrwrightinsures.com for free, with auto-renewing SSL.

---

## Step 6: Set up forms with Formspree (10 min, free)
GitHub Pages serves static files — it cannot process form submissions directly.
Formspree handles this: it receives the POST, emails you, and logs the data. Free tier = 50 submissions/month. Their $8/mo tier is unlimited and adds Sheets export.

For each form (Medicare, Disability, Contact):

1. Go to formspree.io → Create a free account with Mischa@MrWrightInsures.com
2. Click "New Form" → name it (e.g. "Medicare Form")
3. Copy the endpoint URL, looks like: https://formspree.io/f/xabcdefg
4. Open the relevant HTML file in the site/ folder:
   - site/medicare.html → find <form data-lead-form
   - site/disability-insurance.html → find <form data-lead-form
   - site/contact.html → find <form data-lead-form
5. Add the endpoint as an attribute:
   Change: <form data-lead-form
   To:     <form data-lead-form data-endpoint="https://formspree.io/f/YOUR-ID"
6. Save the file, re-upload to GitHub (or git push) — site re-deploys in ~60 seconds
7. Submit a test form on the live site → check your email for the submission

Formspree → Google Sheets: In Formspree dashboard → Integrations → Google Sheets.
Connect to your Website Leads sheet. Formspree maps column names automatically.

---

## Step 7: Future edits (any time)
To change any copy, image, or layout:
1. Edit the file in site/ on your computer (or directly on GitHub.com via the pencil icon)
2. Save/commit to the main branch
3. GitHub Actions re-deploys automatically in ~60 seconds

To add a blog post:
1. Copy an existing file from site/blog/
2. Edit the content
3. Add a link to it in site/resources.html
4. Commit → live in 60 seconds

---

## Google Search Console (after launch, 10 min)
1. Go to search.google.com/search-console
2. Add property → URL prefix → https://mrwrightinsures.com
3. Verify via HTML tag method (add a meta tag to index.html <head>)
4. Submit sitemap: https://mrwrightinsures.com/sitemap.xml

## Cost summary
- GitHub Pages hosting: FREE (forever for public repos)
- GitHub account: FREE
- Formspree free tier: FREE (50 submissions/month)
- Formspree $8/mo: if you exceed 50/month or want Sheets export built-in
- SSL certificate: FREE (auto-renewing via Let's Encrypt)
- Domain (mrwrightinsures.com): you already own it — no new cost
