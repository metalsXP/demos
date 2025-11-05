# showProductionOrder Demo

A simple HTML page that returns a production order after a valid sales order number has been entered.

## Features

- **UI5 Web Components**: Uses official SAP UI5 Web Components for authentic Fiori look and feel
- **SAP Shell Bar**: Standard SAP Fiori application header
- **Form Interface**: Sales order input with production order display
- **No Framework Required**: Pure HTML, CSS, and JavaScript - no React, Vue, or Angular
- **GitHub Pages Ready**: Fully deployable to GitHub Pages

## Interface Components

- **Sales Order Input**: Text input field with label
- **Show Production Order Button**: Action button that displays the production order
- **Production Order Display**: Shows "Production Order: 9000356" when button is clicked

## Local Testing

Opening the file directly (file://) or use a local web server.

```bash
# Node.js serve
npx serve
```

## mXP Recorder

The following test will be recorded.

```typescript
import { test, expect } from '#metalsxp';

test.use({
    viewport: {
        height: 883,
        width: 1564
    }
});

test('showProductionOrder', async ({ page }) => {
  await page.goto('http://localhost:3000/');
  await page.getByRole('spinbutton', { name: 'Sales Order' }).click();
  await page.getByRole('spinbutton', { name: 'Sales Order' }).fill('14143');
  await page.getByRole('button', { name: 'Show Production Order' }).click();
  await expect(page.locator('#resultSection')).toContainText('Production Order: 9000356');
});

// recorded with mXP Recorder
```


Then navigate to `http://localhost:3000` in your browser.

**Troubleshooting**:
- If you see blank components or console errors, ensure you're using HTTP (not file://)
- Check browser console for any 404 errors on CDN resources
- Ensure you're using a modern browser with import map support (Chrome 89+, Safari 16.4+, Firefox 108+)

## Technologies Used

- **UI5 Web Components** (v2.6.3): Official SAP UI5 web component library
- **UI5 Fiori Components** (v2.14.0): SAP Fiori-specific components (ShellBar)
- **Import Maps**: Modern ES6 module loading via jsDelivr CDN
- **SAP Fiori Design**: Following SAP's design guidelines for standard transactions
- **Vanilla JavaScript**: No frameworks or build tools required

## Browser Support

Requires modern browsers with Web Components and Import Maps support:
- Chrome/Edge 89+ (full support)
- Firefox 108+ (full support)
- Safari 16.4+ (full support)

**Note**: Import maps are a relatively new feature. Older browsers will not work.

## Customization

To modify the production order number or add more functionality:

1. Open `index.html`
2. Find the `<ui5-text>` element with id `productionOrderText`
3. Change the text content: `Production Order: 9000356`
4. Add additional form fields by following the same pattern with `ui5-label` and `ui5-input`

## License

This is a demonstration project. Feel free to use and modify as needed.

## Resources

- [UI5 Web Components Documentation](https://sap.github.io/ui5-webcomponents/)
- [SAP Fiori Design Guidelines](https://experience.sap.com/fiori-design-web/)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)
