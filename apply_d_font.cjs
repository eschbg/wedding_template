const fs = require('fs');

function applyTo(file) {
    let css = fs.readFileSync(file, 'utf8');
    
    // revert #w-06fskfrb (Letter D)
    css = css.replace(/#w-06fskfrb \.text-block-css\s*\{[\s\S]*?\}/g, `#w-06fskfrb .text-block-css {
      border-color: rgba(229, 231, 235, 1);
      border-style: solid;
      color: rgba(109, 88, 61, 1.000);
      font-family: 'KD-Aureligena-Script.ttf', sans-serif;
      font-size: 59px;
      text-align: center;
      --type: 0;D
    }`);

    // update #w-cczryo41 text-block-css to KD-Aureligena-Script
    css = css.replace(/#w-cczryo41 \.text-block-css\s*\{[\s\S]*?\}/g, `#w-cczryo41 .text-block-css {
      border-color: rgba(229, 231, 235, 1);
      border-style: solid;
      color: rgba(109, 88, 61, 1.000);
      font-family: 'KD-Aureligena-Script.ttf', sans-serif !important;
      font-size: 65px !important;
      font-weight: normal !important;
      line-height: 1.0 !important;
      text-align: center;
      --type: 0;
    }`);
    
    fs.writeFileSync(file, css);
}

applyTo('public/webcake-styles.css');
applyTo('src/assets/original-webcake.css');

console.log('Applied KD-Aureligena-Script');
