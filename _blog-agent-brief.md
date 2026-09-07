# Brief: scheduled blog drafting agent

Draft ONE blog post for contentcam.app (this repo, a static GitHub Pages site) and open a pull
request. **Do NOT push to main.** Nothing goes live until a human merges.

## About the app

ContentCam is an iPhone and Android camera app that records vertical (9:16) and horizontal (16:9)
video at the same time in one take. It also has Dual Lens mode (two cameras at once, iPhone 11+),
Front / Back mode (both platforms, premium, 5 free recordings), a teleprompter, manual controls
(exposure, white balance 2500-8000K, ISO, shutter), 4K and 60fps, and timelapse. It collects no
analytics: no SDKs, no account. Pricing is monthly, annual with a 7-day free trial, or a one-time
lifetime option. It is built solo in Australia by Jimmy, who is the author of every post.

## Step 1 — pick a topic

Read `_blog-backlog.md`. List the directories under `blog/` and the post titles in
`blog/index.html` so you know what already exists. Pick ONE unpublished topic.

Prefer bucket 1, but rotate: if the two newest posts came from the same bucket, choose a different
bucket. Never duplicate an existing topic under a new slug.

## Step 2 — verify before you write

This is the rule that matters most.

Every factual claim about a named product, company, price, version, specification or date must be
checked against a **live primary source during this run**, using WebSearch and WebFetch. Primary
sources are the App Store or Google Play listing, or the vendor's own specifications page. Cite the
source in the post with the date you checked it.

- If you cannot verify a claim, **cut it**.
- Never state that a product is discontinued, abandoned or unmaintained unless a primary source says
  so. A stale "last updated" date is a fact you may report; "abandoned" is a conclusion you may not.
- Never invent numbers, benchmarks, quotes or review counts.
- Check who currently publishes an app before describing it. Ownership changes.

## Step 3 — write it

Copy the structure of `blog/dualshot-recorder-vs-contentcam/index.html` exactly: the
`@head-common` block, title / description / canonical / og / twitter tags, the BlogPosting and
BreadcrumbList JSON-LD, the `@nav` block, crumbs, `article`, the byline
"By Jimmy, developer of ContentCam", the `post-cta` block and the `@footer` block. Update every URL,
slug, title and date. Use today's date.

**Voice:** direct, specific, honest, first person. Australian and British spelling (colour,
stabilisation, organised). Value first: the post must be genuinely useful to someone who never
installs the app.

- On any post naming a competitor, open with a disclosure that Jimmy builds ContentCam, and include
  a real section on where the other app genuinely wins.
- On purely educational posts, mention ContentCam once at most, or not at all.

**Do not use em dashes.** Avoid: delve, unlock, leverage, seamless, robust, elevate, streamline,
crucial, pivotal, transformative, game-changer, "In today's", "Let's dive in", "It's important to
note", "Furthermore", "Moreover". Avoid the "it's not X, it's Y" construction. Prefer concrete
numbers and specifics over adjectives. Vary sentence length. Do not pad every list to three items.

## Step 4 — wire it up

- `blog/index.html` — add a card, newest first, matching the existing markup exactly
- `sitemap.xml` — add the post with today's `lastmod`, and bump the `/blog/` entry to today
- `llms.txt` — add a line in the blog list
- `llms-full.txt` — add it where the related posts are referenced
- Add a link to the new post from the "Related:" line of 2-3 related existing posts

## Step 5 — open a PR

Create a branch named `blog/<slug>`, commit, push, and open a pull request. The PR body must list:

1. The topic chosen and why
2. Every source URL you verified, and what each one confirmed
3. Anything you could not verify and therefore cut

Do not merge it.
