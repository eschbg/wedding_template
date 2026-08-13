const fs = require('fs');
const file = 'src/components/Gallery.vue';
let content = fs.readFileSync(file, 'utf8');

// Remove QR imports
content = content.replace(/\/\/ --- QR Images ---\r?\nimport brideQr from "\.\.\/assets\/images\/qr-cd\.webp";\r?\nimport groomQr from "\.\.\/assets\/images\/qr-cr\.webp";\r?\n/, '');

// Remove refs and function
content = content.replace(/const showGiftModal = ref\(false\);\r?\nconst zoomedQr = ref\(null\);\r?\n\r?\nconst openZoom = \(imgSrc\) => \{\r?\n  zoomedQr\.value = imgSrc;\r?\n\};\r?\n/, '');

// Remove button
content = content.replace(/        <!-- "GỬI QUÀ MỪNG CƯỚI" button -->[\s\S]*?<\/div>\r?\n        <\/div>\r?\n\r?\n/, '');

// Replace names
content = content.replace(/Bá Nam & Thùy Dung/g, 'Đức Dương & Thanh Hằng');

// Remove modals
content = content.replace(/  <!-- Gift Modal \(QR codes\) -->[\s\S]*?<\/template>/, '</template>');

fs.writeFileSync(file, content);
