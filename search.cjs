const fs = require('fs');
let html = fs.readFileSync('public/original-updated.html', 'utf8');
let match1 = html.indexOf('"06fskfrb"');
if (match1 !== -1) console.log('06fskfrb context:', html.substring(match1 - 20, match1 + 200));
let match2 = html.indexOf('"whvexl1r"');
if (match2 !== -1) console.log('whvexl1r context:', html.substring(match2 - 20, match2 + 200));
