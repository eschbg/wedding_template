const fs = require('fs');

let cssPath = './src/assets/original-webcake.css';
let css = fs.readFileSync(cssPath, 'utf8');

// remove previous block
css = css.replace(/\/\* Apply font of N to D \*\/[\s\S]*?}/g, '');
css = css.replace(/\/\* Apply font of N to D and tweak styles \*\/[\s\S]*?}/g, '');

let cssAddition = `\n\n/* Apply font of N to D and tweak styles */\n#w-06fskfrb .text-block-css {\n  font-family: 'FzQuagera.ttf', sans-serif !important;\n  font-weight: normal !important;\n  font-size: 50px !important;\n}\n#w-whvexl1r .text-block-css {\n  font-weight: normal !important;\n  font-size: 50px !important;\n}\n`;

fs.writeFileSync(cssPath, css + cssAddition);
console.log('Updated: ' + cssPath);

let webcakeCssPath = './public/webcake-styles.css';
if (fs.existsSync(webcakeCssPath)) {
    let webcakeCss = fs.readFileSync(webcakeCssPath, 'utf8');
    webcakeCss = webcakeCss.replace(/\/\* Apply font of N to D \*\/[\s\S]*?}/g, '');
    webcakeCss = webcakeCss.replace(/\/\* Apply font of N to D and tweak styles \*\/[\s\S]*?}/g, '');
    fs.writeFileSync(webcakeCssPath, webcakeCss + cssAddition);
    console.log('Updated: ' + webcakeCssPath);
}
