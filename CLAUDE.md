# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository purpose

GitHub Pages site (`metalsXP/demos`) serving standalone, static HTML demo pages. Each demo is self-contained — vanilla HTML/CSS/JS, no build tools, no package manager, no framework.

## Architecture

- `index.html` at the repo root is a landing page — plain HTML/CSS listing every demo as a linked card (no framework, no build step). When adding a new demo, add a card here pointing at its directory.
- Each demo lives in its own top-level directory (e.g. `showProductionOrder/`, `hildegard/`) containing an `index.html` and a `README.md`. GitHub Pages serves each directory at `https://<pages-domain>/<demo-name>/`.
- Demos are UI mockups, not real integrations: all "backend" behavior (e.g. returning a production order for a sales order number) is hardcoded/simulated in inline `<script>` blocks with a `setTimeout` to mimic network latency — there is no server or API call.
- Demos vary in their UI stack: some (`showProductionOrder/`) use SAP UI5 Web Components (Fiori look and feel) loaded via CDN import maps (jsDelivr); others (`hildegard/`) are plain HTML/CSS/JS with Google Fonts via CDN. Pick whichever fits the demo being built — there's no requirement to use UI5 everywhere.
- A demo can be gated behind a client-side password prompt (see `hildegard/index.html`) when it's an internal preview rather than a public demo. This is enforced entirely in the browser (password checked as a SHA-256 hash, unlocked state cached in `sessionStorage`) — GitHub Pages is static-only, so there's no real server-side auth option. Treat it as a casual deterrent, not real access control: the check logic and hash are visible to anyone who reads the page source.

## Running a demo locally

Import maps require serving over HTTP — opening `index.html` via `file://` will not work.

```bash
npx serve
```

Then open the served demo directory in a browser (Chrome/Edge/Firefox/Safari, recent versions — import map support required).

## Adding a new demo

Follow the pattern established by `showProductionOrder/`:
- New top-level directory with its own `index.html`.
- Self-contained: CDN import map for any UI5 (or other) web components, inline styles, inline scripts — no shared/bundled assets across demos.
- Simulated data/behavior only; don't wire up real backend calls.
- Include a `README.md` describing the demo's purpose and interface.

## Test recordings (mXP Recorder)

Demo READMEs may include a Playwright-style test snippet under an "mXP Recorder" heading (imports from `#metalsxp`). These are recordings of interactions with the demo used by the MetalsXP tooling, not tests run in this repository — there is no local test runner or CI here.
