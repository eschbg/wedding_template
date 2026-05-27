const fs = require('fs');

function applyTo(file) {
    let css = fs.readFileSync(file, 'utf8');
    
    // update #w-cczryo41 text-block-css
    css = css.replace(/#w-cczryo41 \.text-block-css\s*\{[\s\S]*?\}/g, `#w-cczryo41 .text-block-css {
      border-color: rgba(229, 231, 235, 1);
      border-style: solid;
      color: rgba(109, 88, 61, 1.000);
      font-family: 'Great Vibes', cursive !important;
      font-size: 52px !important;
      font-weight: 320 !important;
      line-height: 1.0 !important;
      text-align: center;
      --type: 0;
    }`);
    
    // Remove padding from #w-cczryo41
    css = css.replace(/#w-cczryo41\s*\{[\s\S]*?\}/g, (match) => {
        if (match.includes('.text-block')) return match;
        return `#w-cczryo41 {
      top: 0px;
      left: 0px;
      width: 325px;
      height: auto !important;
    }`;
    });
    
    fs.writeFileSync(file, css);
}

applyTo('public/webcake-styles.css');
applyTo('src/assets/original-webcake.css');

// update vue file to make & smaller proportionately
let vue = fs.readFileSync('src/components/RsvpForm.vue', 'utf8');
vue = vue.replace(/<span style=\"font-size: 40px\">&amp;<\/span>/g, '<span style=\"font-size: 32px\">&amp;</span>');
fs.writeFileSync('src/components/RsvpForm.vue', vue);

console.log('Thinner and smaller');
