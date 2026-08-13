const fs = require('fs');
const path = require('path');

function processDir(dir) {
  const files = fs.readdirSync(dir);
  for (const file of files) {
    const fullPath = path.join(dir, file);
    if (fs.statSync(fullPath).isDirectory()) {
      processDir(fullPath);
    } else if (fullPath.endsWith('.vue') || fullPath.endsWith('.html')) {
      let content = fs.readFileSync(fullPath, 'utf8');
      let originalContent = content;
      
      content = content.replace(/Bá Nam & Thùy Dung/g, 'Đức Dương & Thanh Hằng');
      content = content.replace(/Bá Nam/g, 'Đức Dương');
      content = content.replace(/Thùy Dung/g, 'Thanh Hằng');
      
      content = content.replace(/BÁ NAM & THÙY DUNG/g, 'ĐỨC DƯƠNG & THANH HẰNG');
      content = content.replace(/BÁ NAM/g, 'ĐỨC DƯƠNG');
      content = content.replace(/THÙY DUNG/g, 'THANH HẰNG');
      
      content = content.replace(/06\.06\.2026/g, '20.09.2026');
      content = content.replace(/06-06-2026/g, '20-09-2026');
      content = content.replace(/06\/06/g, '20/09');
      // Fix some potential remaining dates
      
      if (content !== originalContent) {
        fs.writeFileSync(fullPath, content);
        console.log(`Updated ${fullPath}`);
      }
    }
  }
}

processDir('src');
