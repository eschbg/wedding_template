const fs = require('fs');
const path = require('path');

const filePath = path.join(__dirname, '../public/original-updated.html');
const content = fs.readFileSync(filePath, 'utf8');

// Get the body content
const bodyMatch = content.match(/<body[^>]*>([\s\S]*)<\/body>/i);
if (!bodyMatch) {
  console.log("No body found");
  process.exit(1);
}

const bodyContent = bodyMatch[1];
console.log("Body length:", bodyContent.length);

// Let's write a simple parser to find the top-level divs under #webcake-render-root
const renderRootStart = bodyContent.indexOf('id="webcake-render-root"');
if (renderRootStart === -1) {
  console.log("No webcake-render-root found");
  // Let's look for any top level divs
  // In our previous output we saw divs starting at index 244655: Div ID: w-4hid1bt8, w-utq42110...
  // Let's print their HTML tags
} else {
  console.log("webcake-render-root found");
}

// Let's parse the children of body
// Usually they are in a structure like:
// <div id="loading-gate" ...></div>
// <div id="w-..." class="section-...">...</div>
// Let's write a script that output first 2000 chars after <body>
console.log("First 4000 characters of body:\n", bodyContent.substring(0, 4000));
