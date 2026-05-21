const fs = require('fs');
const path = require('path');

const filePath = path.join(__dirname, '../public/original-updated.html');
const content = fs.readFileSync(filePath, 'utf8');

// Find the section w-fi0xg7tu
const startIdx = content.indexOf('id="w-fi0xg7tu"');
if (startIdx === -1) {
  console.log("Section w-fi0xg7tu not found");
  process.exit(1);
}

// Let's find the closing tag of this section
// A section has structure: <div id="w-fi0xg7tu" class="com-section" data-section><div class="section-wrapper ...">...</div></div>
// Let's find the next com-section or end of pageview
const nextSectionIdx = content.indexOf('id="w-o94okgr4"', startIdx);
const sectionHtml = content.substring(startIdx - 50, nextSectionIdx - 50);

console.log("Section 6 HTML length:", sectionHtml.length);

// Print all direct children divs inside the section container
const childRegex = /<div\s+id="([^"]+)"\s+class="([^"]+)"/g;
let match;
while ((match = childRegex.exec(sectionHtml)) !== null) {
  console.log(`Child ID: ${match[1]}, Class: ${match[2]}`);
}
