# Production Release — Week 8 Day 5

A responsive static demo package for documenting a production release handoff. It includes a small interactive release-readiness page, static-host configuration, a demo narration, and a pull-request template.

## Features
- Responsive release-readiness dashboard
- Browser-side smoke checks for page title, heading, stylesheet, JavaScript, and viewport metadata
- Interactive checklist for deployment and handoff tasks
- Deployment configuration for Vercel and Render static hosting

## Tech stack
HTML5, CSS3, Vanilla JavaScript, Vercel static deployment configuration, Render static-site configuration.

## Run locally
Open `index.html` in a browser. No package installation or build step is required.

## Deploy
### Vercel
1. Import the repository into Vercel.
2. Set the project root to this folder if it is inside a larger repository.
3. Choose **Other** as the framework preset.
4. Leave build command blank and set output directory to `.`.
5. Deploy, then test the generated URL.

### Render
1. Create a **Static Site** and connect the repository.
2. Set the root directory to this folder if needed.
3. Leave build command blank and set publish directory to `.`.
4. Deploy, then test the generated URL.

## Deployment URL
**Not deployed yet.** Add the real production URL here after publishing. No hosting account was connected during preparation.

## Verification status
- The source package is structured as a static site.
- The included button runs browser-side checks only.
- A live production URL, provider logs, server-side 500 responses, and all features of any separate existing backend have **not** been verified by this package.
- This demo has no backend, database, authentication, or API integration.

## Known limitations
- This is a standalone static demo, not a copy of a separately existing application unless its source is added.
- The checklist is not persisted.
- Client-side checks cannot confirm deployment health or server logs.
- The demo video and final GitHub pull request must be created after the actual deployment and recording links are available.

## Demo and pull request
See `DEMO_SCRIPT.md` and `PULL_REQUEST_TEMPLATE.md`.
