# To-do (system improvements)

- [ ] **Inbox for manually saved sources.** Add an `inbox/` folder: owner saves pages the agents
      can't open (Reddit, paywalled articles) as PDF/text with the original URL; Gatherer processes
      `inbox/` at the start of each run (extract, grade, dedupe, record link) and moves done files
      to `inbox/done/`. First candidate: r/roasting "First roast Skywalker V2" (registry: needs-manual).
      Also: Home-Barista threads now sit behind a Cloudflare human check (5 threads registered
      needs-manual in run 2026-10-16 #3; top two: "Bean Temperature at First Crack" t99923,
      "Development time of light roasts" t73248).
