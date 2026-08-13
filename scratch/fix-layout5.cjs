const fs = require('fs');
const path = require('path');

const cssFiles = [
  'src/assets/original-webcake.css',
  'src/style.css'
];

const updates = {
  'w-979kjzgs': { top: 140 },
  'w-489q168n': { top: 238 },
  'w-hhef3z1p': { top: 270 },
  'w-9r1np7f9': { top: 317 },
  'w-0sgx4h10': { top: 446 },
  'w-u5974ugb': { top: 483 },
  'w-fy3iaj6k': { top: 585 },
  'w-9xkpyyyd': { top: 663 },
  'w-2bs8c2lb': { height: 813 }
};

for (const file of cssFiles) {
  if (!fs.existsSync(file)) continue;
  let content = fs.readFileSync(file, 'utf8');
  let changed = false;

  for (const [id, styles] of Object.entries(updates)) {
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
