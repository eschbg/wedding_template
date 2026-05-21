const fs = require('fs');
const path = require('path');

const htmlPath = path.join(__dirname, '../public/original-updated.html');
const cssPath = path.join(__dirname, '../src/assets/original-webcake.css');

const content = fs.readFileSync(htmlPath, 'utf8');

// Find all <style> blocks
const styleRegex = /<style[^>]*>([\s\S]*?)<\/style>/gi;
let match;
let cssContent = '';

while ((match = styleRegex.exec(content)) !== null) {
  cssContent += match[1] + '\n\n';
}

console.log("Extracted CSS length:", cssContent.length);

// Ensure the directory exists
const dir = path.dirname(cssPath);
if (!fs.existsSync(dir)) {
  fs.mkdirSync(dir, { recursive: true });
}

fs.writeFileSync(cssPath, cssContent, 'utf8');
console.log("Successfully wrote CSS to", cssPath);
