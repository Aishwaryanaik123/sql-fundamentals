# Release Ready — Production Release Demo

A responsive static web demo for demonstrating release verification, basic interactivity, and deployment readiness.

## Features
- Responsive layout for desktop and mobile
- Demo service status and refresh interaction
- Add, complete, filter, and remove issue items
- Release checklist
- Client-side form validation
- No backend or database required

## Tech stack
HTML5, CSS3, Vanilla JavaScript.

## Run locally
Open `index.html` in a modern browser. No package installation or build step is required.

## Deploy
This is a static site and can be deployed from this folder to Vercel, Netlify, or a static hosting service.

### Vercel
1. Create/import a Git repository containing `index.html`, `style.css`, and `script.js` at the repository root.
2. In Vercel, choose **Other** as the framework preset.
3. Leave the build command empty and set the output directory to `.` if prompted.
4. Deploy, then open the generated URL and run the verification checklist in `DEPLOYMENT_CHECKLIST.md`.

**Deployment URL:** Not deployed by this package. Add the real URL after deployment.

## Verification
See `DEPLOYMENT_CHECKLIST.md`. The app is static and does not make backend/API requests, so it has no application API endpoints that can return HTTP 500. Hosting/platform errors still need to be checked on the actual deployed URL.

## Demo video
Use `DEMO_SCRIPT.md` as a 3-minute narration and recording plan. A real recording is not included because it must capture the deployed site and its actual URL.

## Pull request
Use `PULL_REQUEST_TEMPLATE.md` as the final PR description. Replace placeholders with the real repository, deployment URL, and demo link.

## Known limitations
- Demo data is stored only in browser memory and resets on refresh.
- Status indicators are illustrative; they do not monitor real infrastructure.
- No authentication, backend, database, or API integration.
- Deployment URL and demo recording must be added after the actual deployment.
