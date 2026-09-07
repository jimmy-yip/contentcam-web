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

**This section is your only source of truth for ContentCam.** Do not attribute a feature, price,
platform or limitation to it that is not written above. If you want to say the app does something and
it is not listed here, either leave it out or check the site's own `/features/` pages.

## Hard constraint: you cannot verify product facts in this environment

The sandbox egress proxy blocks `apps.apple.com`, `play.google.com`, `support.google.com`,
`help.instagram.com` and `support.tiktok.com`. Confirmed 2026-09-07. WebSearch works, but it returns
SEO content blogs, which are **not** acceptable sources for a factual claim.

Reachable and useful: `developer.apple.com`, `developer.android.com`, `github.com`. Also blocked:
**contentcam.app itself**, so never try to fetch the live site. Read the files in this repo instead.

Therefore:

- **Do not write any post that depends on a named product's version, price, publisher, feature list,
  release date or maintenance status.** You cannot check those here, and a wrong claim about a real
  company's product on a live site is the worst outcome this job can produce.
- **Do not state a platform specification as a number** (resolution, file size cap, maximum length,
  bitrate) unless you reached the platform's own documentation. If it is blocked, describe the thing
  qualitatively instead, or drop that section.
- Never invent numbers, benchmarks, prices, quotes or review counts. Not once, not as a placeholder.
- If the topic you picked turns out to need any of the above, **abandon it and pick another.** An
  honest "I picked a different topic because I could not verify X" in the PR body is a good outcome.

Competitor and app-comparison posts are handled by a human in a session with working access. They are
not your job. Do not attempt them even if they sit unpublished in the backlog.

## Step 1 — pick a topic

Read `_blog-backlog.md`. Only pick from the sections marked **CLOUD-SAFE**. Ignore every section
marked **LOCAL ONLY**, no matter how attractive the topic looks.

List the directories under `blog/` and the post titles in `blog/index.html` so you know what already
exists. Pick ONE unpublished topic. Rotate: if the two newest posts came from the same section,
choose a different one. Never duplicate an existing topic under a new slug.

## Step 2 — sourcing: craft knowledge, not search results

The cloud-safe topics are evergreen technique: lighting, audio, composition, frame rates, workflow,
filming for a niche, the business of UGC. They do not need a live source, and that is exactly why
they are the ones you have been given.

Be concrete anyway. Real settings, real reasons, real trade-offs. "Set white balance to about 5600K
outdoors and lock it" beats "adjust your settings appropriately". Specificity is the whole value of
the post. Draw it from established filming practice, not from a search result.

If you genuinely need to check something and the source is reachable, do check it and cite it with
the date. If it is blocked, work around it as described above.

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
4. If fewer than about 8 unpublished CLOUD-SAFE topics remain in the backlog, say so plainly at the
   top of the PR body so a human knows to top it up

Do not merge it.

## If the push is refused

`git push` may return 403 ("Claude doesn't have GitHub access to this repository"), and the GitHub
MCP integration may be read-only. If that happens, do not treat the run as failed and do not retry
in a loop. Instead:

1. Commit everything on the local branch as normal.
2. Run `git format-patch main --stdout > <scratchpad>/<branch-name>.patch`.
3. Send the patch and the new post file to the user with SendUserFile, with a caption giving the
   apply command: `git checkout -b <branch> && git am < <branch>.patch`
4. State plainly in your final message that the PR could not be opened, quote the exact error, and
   say the fix is installing the Claude GitHub App or reconnecting GitHub with write access.

The container is ephemeral, so work that is only committed locally is lost. Sending the patch is
what makes the run worth having.

## Fix what your own checks find

Before committing, grep your post for em dashes, the banned words listed above, and US spellings
(color, organize, stabilize, favorite, center). **Fix every hit.** Reporting a problem you found and
leaving it in the file is not acceptable.
