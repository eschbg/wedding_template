const fs = require('fs');
const path = require('path');

const cssPath = path.join(__dirname, '../src/assets/original-webcake.css');
const content = fs.readFileSync(cssPath, 'utf8');

const regex = /background-image:\s*url\((.*?)\)/g;
let match;
let count = 0;
while ((match = regex.exec(content)) !== null) {
  console.log(`Match #${++count}: ${match[1]}`);
}
