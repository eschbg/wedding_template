const fs = require('fs');
let vue = fs.readFileSync('src/components/RsvpForm.vue', 'utf8');

// The current span is: <span style="font-size: 24px; line-height: 1.0; margin: -5px 0;">&amp;</span>
// We will replace it to move & up significantly towards "Bá Nam" (margin-top: -30px)
vue = vue.replace(/<span style=\"font-size: 24px; line-height: 1\.0; margin: -5px 0;\">&amp;<\/span>/g, '<span style=\"font-size: 24px; line-height: 1.0; margin-top: -30px; margin-bottom: -5px;\">&amp;</span>');

fs.writeFileSync('src/components/RsvpForm.vue', vue);
console.log('Adjusted ampersand position');
