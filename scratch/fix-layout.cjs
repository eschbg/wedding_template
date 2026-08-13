const fs = require('fs');
const path = require('path');

const cssFiles = [
  'src/assets/original-webcake.css',
  'src/style.css'
];

const updates = {
  'w-489q168n': { top: 696.5 },
  'w-hhef3z1p': { top: 722.5 },
  'w-9r1np7f9': { top: 746.5 },
  'w-0sgx4h10': { top: 852.5 },
  'w-u5974ugb': { top: 883.5, height: 57.6 },
  'w-fy3iaj6k': { top: 941.5 },
  'w-9xkpyyyd': { top: 1007.5 },
  'w-2bs8c2lb': { height: 1100 }
};

for (const file of cssFiles) {
  if (!fs.existsSync(file)) continue;
  let content = fs.readFileSync(file, 'utf8');
  let changed = false;

  for (const [id, styles] of Object.entries(updates)) {
    // We want to replace properties ONLY inside the `#id { ... }` block.
    // The CSS might have `.desktop #id { ... }` or `@media ... #id { ... }`.
    // We can use a regex to find the block for `#id { ... }` and update inside it.
    // A simpler way: just replace `top: <number>px;` globally for that ID block.
    
    // Regex to match `#id { ... }` ignoring nested blocks, but webcake CSS usually has flat blocks like `#id { top: ... }`.
    const blockRegex = new RegExp(`(#${id}\\s*\\{[^}]*?\\})`, 'g');
    
    content = content.replace(blockRegex, (match) => {
      let newBlock = match;
      if (styles.top !== undefined) {
        newBlock = newBlock.replace(/top:\s*[-0-9.]+px/, `top: ${styles.top}px`);
      }
      if (styles.height !== undefined) {
        newBlock = newBlock.replace(/height:\s*[-0-9.]+px/, `height: ${styles.height}px`);
      }
      return newBlock;
    });
    changed = true;
  }
  
  if (changed) {
    fs.writeFileSync(file, content);
    console.log(`Updated ${file}`);
  }
}
