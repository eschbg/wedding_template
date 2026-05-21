const fs = require('fs');
const path = require('path');

const filePath = path.join(__dirname, '../public/original.html');
const content = fs.readFileSync(filePath, 'utf8');

// Find all matches for gate-overlay or gate-wing in CSS
const styleRegex = /<style[^>]*>([\s\S]*?)<\/style>/gi;
let match;
let found = false;
while ((match = styleRegex.exec(content)) !== null) {
  const css = match[1];
  if (css.includes('gate-overlay') || css.includes('gate-wing')) {
    console.log("Found gate styles in original.html style block!");
    console.log(css.substring(css.indexOf('gate-overlay') - 100, css.indexOf('gate-overlay') + 500));
    found = true;
  }
}

if (!found) {
  console.log("Gate styles not found in original.html style blocks.");
}
