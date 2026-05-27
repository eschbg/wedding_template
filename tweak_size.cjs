const fs = require('fs');

let cssPath = './src/assets/original-webcake.css';
let css = fs.readFileSync(cssPath, 'utf8');

// replace 50px with 54px in the custom block
css = css.replace(/font-size: 50px !important;/g, 'font-size: 54px !important;');

fs.writeFileSync(cssPath, css);
console.log('Updated: ' + cssPath);

let webcakeCssPath = './public/webcake-styles.css';
if (fs.existsSync(webcakeCssPath)) {
    let webcakeCss = fs.readFileSync(webcakeCssPath, 'utf8');
    webcakeCss = webcakeCss.replace(/font-size: 50px !important;/g, 'font-size: 54px !important;');
    fs.writeFileSync(webcakeCssPath, webcakeCss);
    console.log('Updated: ' + webcakeCssPath);
}
