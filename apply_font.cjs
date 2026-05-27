const fs = require('fs');

let cssAddition = `\n\n/* Apply font of N to D */\n#w-06fskfrb .text-block-css {\n  font-family: 'FzQuagera.ttf', sans-serif !important;\n  font-weight: bold !important;\n}\n`;

let cssPath = './src/assets/original-webcake.css';
let css = fs.readFileSync(cssPath, 'utf8');
if (!css.includes('Apply font of N to D')) {
    fs.writeFileSync(cssPath, css + cssAddition);
    console.log('Updated: ' + cssPath);
}

let webcakeCssPath = './public/webcake-styles.css';
if (fs.existsSync(webcakeCssPath)) {
    let webcakeCss = fs.readFileSync(webcakeCssPath, 'utf8');
    if (!webcakeCss.includes('Apply font of N to D')) {
        fs.writeFileSync(webcakeCssPath, webcakeCss + cssAddition);
        console.log('Updated: ' + webcakeCssPath);
    }
}
