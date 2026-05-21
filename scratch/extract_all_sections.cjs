const fs = require('fs');
const path = require('path');

const htmlPath = path.join(__dirname, '../public/original-updated.html');
const content = fs.readFileSync(htmlPath, 'utf8');

// Find all sections
const sectionRegex = /<div\s+id="([^"]+)"\s+class="com-section" data-section>/g;
const sections = [];
let match;
while ((match = sectionRegex.exec(content)) !== null) {
  sections.push({ id: match[1], index: match.index });
}

sections.forEach((sec, idx) => {
  const nextIndex = idx + 1 < sections.length ? sections[idx + 1].index : content.indexOf('</body>');
  let secHtml = content.substring(sec.index, nextIndex).trim();
  
  // Clean up any trailing code or trailing elements if needed
  // For the last section, make sure we only grab until the closing pageview div
  if (idx === sections.length - 1) {
    const closePageview = secHtml.indexOf('</div>\n    <div id="w-__popup_default__"');
    if (closePageview !== -1) {
      secHtml = secHtml.substring(0, closePageview).trim();
    }
  }

  const destPath = path.join(__dirname, `../scratch/section_${idx + 1}_${sec.id}.html`);
  fs.writeFileSync(destPath, secHtml, 'utf8');
  console.log(`Wrote Section #${idx + 1} (${sec.id}) to ${destPath}`);
});
