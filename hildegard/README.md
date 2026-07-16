# hildegard (pulseXP mockup)

An internal go-to-market mockup landing page for **pulseXP**, metalsXP's SAP test-automation product. Single self-contained `index.html` — no build tools, no framework.

## Access

This page is gated behind a client-side password prompt, since it's an internal preview, not a public product page:

- **Username**: `hildegard`
- **Password**: `mXPTesting2026!`

The password is checked in the browser against a SHA-256 hash (not stored in plaintext in the page source), and access is cached in `sessionStorage` for the rest of the browser session. GitHub Pages is static hosting only — there is no server-side Basic Auth available, so this JS gate is the closest equivalent. It deters casual visitors but is not real security: anyone who reads the script can see the check being performed, and a determined visitor could brute-force the hash offline. Do not put anything genuinely sensitive on this page.

## Local Testing

Import maps and `crypto.subtle` both require a secure context, so open this via a local server, not `file://`.

```bash
npx serve
```

## Technologies Used

- Vanilla HTML/CSS/JS — no framework or build step
- Google Fonts (Inter) via CDN
- `crypto.subtle` (Web Crypto API) for the client-side password check
- `IntersectionObserver` for scroll-reveal animations

## Customization

The color palette is defined as CSS custom properties at the top of `index.html` (`--ds-primary`, `--ds-secondary`, `--ds-success-title`, `--color-secondary-dark`, `--ds-error-title`, `--ds-alert`, `--ds-info-title`, etc.) — update those to re-theme the whole page.
