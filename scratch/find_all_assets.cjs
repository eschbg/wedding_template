const fs = require('fs');
const path = require('path');

const filePath = path.join(__dirname, '../public/original-updated.html');
const content = fs.readFileSync(filePath, 'utf8');

const regex = /https:\/\/statics\.pancake\.vn\/[^\s'")]*/g;
const matches = [...new Set(content.match(regex))];

console.log("All static assets in original-updated.html:");
matches.forEach((url, i) => {
  console.log(`#${i + 1}: ${url}`);
});
