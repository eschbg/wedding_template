const fs = require('fs');
const path = require('path');

const htmlPath = path.join(__dirname, '../public/original-updated.html');
const outputPath = path.join(__dirname, '../public/webcake-styles.css');

const content = fs.readFileSync(htmlPath, 'utf8');

// Extract all style blocks
const styleRegex = /<style[^>]*>([\s\S]*?)<\/style>/gi;
let match;
let cssContent = '';

while ((match = styleRegex.exec(content)) !== null) {
  cssContent += match[1] + '\n\n';
}

// Add the gate CSS (not found in style blocks - must have been in external CDN css)
const gateCSS = `
/* ===== GATE ANIMATION CSS ===== */
.gate-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 999999;
  overflow: hidden;
  pointer-events: none;
}

.gate-wing {
  position: absolute;
  top: 0;
  height: 100%;
  background-size: cover;
  background-repeat: no-repeat;
  transition: transform 3.0s cubic-bezier(0.6, 0.5, 0.45, 1);
}

.left-wing {
  left: 0;
  width: 65%;
  background-position: right center;
}

.right-wing {
  right: 0;
  width: 55%;
  background-position: left center;
}

.gate-overlay.open .left-wing {
  transform: translateX(-100%);
}

.gate-overlay.open .right-wing {
  transform: translateX(100%);
}
/* ===== END GATE ANIMATION CSS ===== */
`;

// Override lazy loading - we want images to show immediately in Vue
const lazyOverride = `
/* ===== OVERRIDE LAZY LOADING ===== */
/* In original site, .lazy hides backgrounds until JS loads them.
   In our Vue app, we don't need lazy loading - show everything immediately */
.lazy {
  background: inherit !important;
  -webkit-mask-image: inherit !important;
}
/* ===== END OVERRIDE ===== */
`;

// Combine all CSS
const finalCSS = cssContent + gateCSS + lazyOverride;

fs.writeFileSync(outputPath, finalCSS, 'utf8');
console.log(`Generated webcake-styles.css (${Math.round(finalCSS.length / 1024)}KB)`);
console.log(`Output: ${outputPath}`);
