const fs = require('fs');

function applyTo(file) {
    let css = fs.readFileSync(file, 'utf8');
    
    // update #w-cczryo41 text-block-css size to 75px
    css = css.replace(/font-size: \d+px !important;/g, (match, offset, fullString) => {
        // We want to make sure we only replace in #w-cczryo41
        // It's safer to just re-inject the whole block
        return match;
    });
    
    css = css.replace(/#w-cczryo41 \.text-block-css\s*\{[\s\S]*?\}/g, `#w-cczryo41 .text-block-css {
      border-color: rgba(229, 231, 235, 1);
      border-style: solid;
      color: rgba(109, 88, 61, 1.000);
      font-family: 'KD-Aureligena-Script.ttf', sans-serif !important;
      font-size: 78px !important;
      font-weight: normal !important;
      line-height: 1.0 !important;
      text-align: center;
      --type: 0;
    }`);
    
    // but preserve the color #cc0000 !important;
    css = css.replace(/color: rgba\(109, 88, 61, 1\.000\);/g, 'color: #cc0000 !important;');
    
    fs.writeFileSync(file, css);
}

applyTo('public/webcake-styles.css');
applyTo('src/assets/original-webcake.css');

// Adjust the ampersand size in Vue file to 32px
let vue = fs.readFileSync('src/components/RsvpForm.vue', 'utf8');
// The span might have 45px or something else
vue = vue.replace(/<span style=\"font-size: \d+px\">&amp;<\/span>/g, '<span style=\"font-size: 32px\">&amp;</span>');
fs.writeFileSync('src/components/RsvpForm.vue', vue);

console.log('Adjusted sizes: Names 78px, & 32px');
