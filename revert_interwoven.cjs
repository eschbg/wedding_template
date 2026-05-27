const fs = require('fs');

let vue = fs.readFileSync('src/components/StoryTimeline.vue', 'utf8');

// Revert D block inline styles
vue = vue.replace(
    /<div id="w-06fskfrb" class="com-text-block p-absolute is-animation" style="[^"]*">/,
    `<div id="w-06fskfrb" class="com-text-block p-absolute is-animation">`
);
vue = vue.replace(
    /<h2 class="text-block-css full-width" style="[^"]*">D<\/h2>/,
    `<h2 class="text-block-css full-width">D</h2>`
);

// Revert N block inline styles
vue = vue.replace(
    /<div id="w-whvexl1r" class="com-text-block p-absolute is-animation" style="[^"]*">/,
    `<div id="w-whvexl1r" class="com-text-block p-absolute is-animation">`
);
vue = vue.replace(
    /<h2 class="text-block-css full-width" style="[^"]*">N<\/h2>/,
    `<h2 class="text-block-css full-width">N</h2>`
);

fs.writeFileSync('src/components/StoryTimeline.vue', vue);

// Now CSS files
function applyTo(file) {
    let css = fs.readFileSync(file, 'utf8');
    
    // Revert font-family for D
    css = css.replace(/#w-06fskfrb \.text-block-css\s*\{[^}]*\}/g, (match) => {
        return `#w-06fskfrb .text-block-css {
      border-color: rgba(229, 231, 235, 1);
      border-style: solid;
      color: rgba(109, 88, 61, 1.000);
      font-family: 'KD-Aureligena-Script.ttf', sans-serif !important;
      font-size: 59px !important;
      font-weight: normal !important;
      text-align: center;
      --type: 0;
    }`;
    });
    
    css = css.replace(/#w-06fskfrb\.animation \.text-block-css\s*\{[^}]*\}/g, (match) => {
        return `#w-06fskfrb.animation .text-block-css {
      border-color: rgba(229, 231, 235, 1);
      border-style: solid;
      color: rgba(109, 88, 61, 1.000);
      font-family: 'KD-Aureligena-Script.ttf', sans-serif !important;
      font-size: 59px !important;
      font-weight: normal !important;
      text-align: center;
      --type: 0;
    }`;
    });

    // Restore original positions
    css = css.replace(/#w-whvexl1r\s*\{[^}]*\}/g, `#w-whvexl1r {
      top: 32.07810592651367px !important;
      left: 130.01376342773438px !important;
      width: 128px;
      height: 90.00000762939453px;
    }`);
    
    css = css.replace(/#w-06fskfrb\s*\{[^}]*\}/g, `#w-06fskfrb {
      top: 44.0572624206543px !important;
      left: 145.01376342773438px !important;
      width: 128px;
      height: 88.48958587646484px;
    }`);

    fs.writeFileSync(file, css);
}

applyTo('public/webcake-styles.css');
applyTo('src/assets/original-webcake.css');

console.log('Reverted to interwoven cursive/serif monogram');
