const fs = require('fs');
const path = require('path');

const filePath = path.join(__dirname, '../public/original-updated.html');
const content = fs.readFileSync(filePath, 'utf8');

// Find all top-level divs under #webcake-render-root
// Or search for class="section-..." or similar
const matches = [];
const regex = /<div\s+[^>]*id="([^"]+)"[^>]*class="[^"]*section-wrapper[^"]*"/g;
let match;
while ((match = regex.exec(content)) !== null) {
  matches.push({ id: match[0], index: match.index });
}

console.log("Found sections:", matches.map(m => m.id));
