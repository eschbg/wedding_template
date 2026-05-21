const fs = require('fs');
const path = require('path');

const filePath = path.join(__dirname, '../public/original-updated.html');
const content = fs.readFileSync(filePath, 'utf8');

// Find all divs with class com-section
const sectionRegex = /<div\s+[^>]*id="([^"]+)"[^>]*class="[^"]*com-section[^"]*"[^>]*>/g;
let match;
const sections = [];
while ((match = sectionRegex.exec(content)) !== null) {
  sections.push({ id: match[1], index: match.index });
}

console.log("Found sections:");
sections.forEach((sec, idx) => {
  // Find start of next section or end of body
  const nextIndex = idx + 1 < sections.length ? sections[idx + 1].index : content.length;
  const secContent = content.substring(sec.index, nextIndex);
  
  // Look for text contents inside this section to identify what it is
  const textMatches = [...secContent.matchAll(/<h[1-6][^>]*>([\s\S]*?)<\/h[1-6]>/g)].map(m => m[1].replace(/<br>/g, ' ').trim());
  const cleanTexts = textMatches.filter(t => t.length > 0).slice(0, 4);
  
  console.log(`Section #${idx + 1}: ID=${sec.id}`);
  console.log(`  Texts:`, cleanTexts);
});
