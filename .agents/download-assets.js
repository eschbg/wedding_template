const fs = require('fs');
const path = require('path');
const https = require('https');

const baseDir = path.resolve(__dirname, '..');
const imagesDir = path.join(baseDir, 'src', 'assets', 'images');
const fontsDir = path.join(baseDir, 'src', 'assets', 'fonts');
const audioDir = path.join(baseDir, 'src', 'assets', 'audio');

// Ensure directories exist
fs.mkdirSync(imagesDir, { recursive: true });
fs.mkdirSync(fontsDir, { recursive: true });
fs.mkdirSync(audioDir, { recursive: true });

const assets = [
  {
    url: 'https://statics.pancake.vn/web-media/6c/e1/93/76/f45d539757d91d0ce0c9476a9cf7307766321a70803b296fd4b970fd-w:1080-h:1920-l:2041770-t:image/png.png',
    dest: path.join(imagesDir, 'gate-left.png')
  },
  {
    url: 'https://statics.pancake.vn/web-media/58/4c/24/bf/63c9c5e1792d6196c8ac3d5f9ba47d083fb0365a33da2a8f46500223-w:1080-h:1920-l:2114080-t:image/png.png',
    dest: path.join(imagesDir, 'gate-right.png')
  },
  {
    url: 'https://statics.pancake.vn/web-media/93/b0/e2/03/74f2d32c1cc49fcf65587c7eeca16d94d1063d40fc34986dcc542e41-w:4024-h:6048-l:11053771-t:image/jpeg.jpg',
    dest: path.join(imagesDir, 'gallery-0.jpg')
  },
  {
    url: 'https://statics.pancake.vn/web-media/cb/f0/e5/4e/0cd0eca1c60fba0ac4808be2ddb9949f18d008f0a48e05b590d3131c-w:4024-h:6048-l:13697850-t:image/jpeg.jpg',
    dest: path.join(imagesDir, 'gallery-1.jpg')
  },
  {
    url: 'https://statics.pancake.vn/web-media/a6/26/d2/71/8a86cbf3db66ba89c0c0cf9f4b7f5479c1b6b9af5d84a52a697678c1-w:4024-h:6048-l:13468349-t:image/jpeg.jpg',
    dest: path.join(imagesDir, 'gallery-2.jpg')
  },
  {
    url: 'https://statics.pancake.vn/web-media/93/65/d1/22/2aaad86c7da43118689d1b08e8808b7fb30a1aa6fbecc193ebd85a27-w:4024-h:6048-l:9881747-t:image/jpeg.jpg',
    dest: path.join(imagesDir, 'gallery-3.jpg')
  },
  {
    url: 'https://statics.pancake.vn/web-media/36/cb/e9/43/c6a79c6b92432af1bf4ea28ce455214f6e258eea5f94d159437778ea-w:4024-h:6048-l:7989599-t:image/jpeg.jpg',
    dest: path.join(imagesDir, 'gallery-4.jpg')
  },
  {
    url: 'https://statics.pancake.vn/web-media/db/36/fe/1d/da7aaefe3000e5c318162b1e7a73bb34f3968e37ce18224664295ed7-w:1748-h:1240-l:294401-t:image/png.png',
    dest: path.join(imagesDir, 'countdown-bg.png')
  },
  {
    url: 'https://statics.pancake.vn/web-media/57/fb/0f/1e/0cce72441eea0138102968975a0069ff1fae66f3a1bff88f51623214-w:1748-h:1240-l:148351-t:image/png.png',
    dest: path.join(imagesDir, 'countdown-flower.png')
  },
  {
    url: 'https://statics.pancake.vn/web-media/af/27/c2/bc/b62e8d89c4cdedbf6b0cd54293760b1220ac60fba39b87f3e943ad38-w:1748-h:1240-l:955071-t:image/png.png',
    dest: path.join(imagesDir, 'rsvp-bg.png')
  },
  {
    url: 'https://statics.pancake.vn/web-media/bc/16/6d/02/8fb7c4176bb80f2a86be09605f32949438cb9b882e939a2619d24423-w:1748-h:1240-l:324842-t:image/png.png',
    dest: path.join(imagesDir, 'thank-you-bg.png')
  },
  {
    url: 'https://statics.pancake.vn/web-media/80/a2/6e/31/7becb89f9e193a78188a114c4c0d4edb9fc2c1d5c5586543dad3ad38-w:6048-h:4024-l:10057816-t:image/jpeg.jpg',
    dest: path.join(imagesDir, 'groom-qr.jpg')
  },
  {
    url: 'https://statics.pancake.vn/web-media/01/46/ff/38/67248371a95d029daf09d3202ffb8fd24dc4280e5127b5750d6466c6-w:656-h:1280-l:77036-t:image/jpeg.jpg',
    dest: path.join(imagesDir, 'bride-qr.jpg')
  },
  {
    url: 'https://statics.pancake.vn/web-media/56/4c/0f/77/eb1d93899f7058a0b85f4dfdeb51e6fee3dd2aab31ab7c0870264160-w:512-h:512-l:19624-t:image/png.png',
    dest: path.join(imagesDir, 'music-disc.png')
  },
  {
    url: 'https://statics.pancake.vn/web-media/c4/68/33/61/e5451e6a75e2c8b4be6bde3f935a05ee7f7f42e98e508107d8c4f8db-w:0-h:0-l:8859163-t:audio/mpeg.mp3',
    dest: path.join(audioDir, 'background-music.mp3')
  }
];

function downloadFile(url, dest) {
  return new Promise((resolve, reject) => {
    const file = fs.createWriteStream(dest);
    https.get(url, (response) => {
      if (response.statusCode !== 200) {
        reject(new Error(`Failed to download: ${url} (Status Code: ${response.statusCode})`));
        return;
      }
      response.pipe(file);
      file.on('finish', () => {
        file.close(() => {
          console.log(`Successfully downloaded to ${path.relative(baseDir, dest)}`);
          resolve();
        });
      });
    }).on('error', (err) => {
      fs.unlink(dest, () => {});
      reject(err);
    });
  });
}

async function fetchGoogleFonts() {
  console.log('Fetching Google Fonts...');
  const fontsUrl = 'https://fonts.googleapis.com/css?family=Roboto:100,300,400,700,900|Taviraj:100,300,400,700,900|Dancing%20Script:100,300,400,700,900&display=swap';
  
  // We need to request with a modern User-Agent to get woff2 format links
  const options = {
    headers: {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36'
    }
  };

  return new Promise((resolve, reject) => {
    https.get(fontsUrl, options, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', async () => {
        try {
          // Parse all url(...) links
          const fontUrls = [...data.matchAll(/url\((.*?)\)/g)].map(m => m[1].replace(/['"]/g, ''));
          console.log(`Found ${fontUrls.length} font files to download.`);
          
          let downloadedCount = 0;
          for (let i = 0; i < fontUrls.length; i++) {
            const fontUrl = fontUrls[i];
            const parsedUrl = new URL(fontUrl);
            const fontFileName = path.basename(parsedUrl.pathname);
            const dest = path.join(fontsDir, fontFileName);
            
            try {
              await downloadFile(fontUrl, dest);
              downloadedCount++;
            } catch (err) {
              console.error(`Failed to download font: ${fontUrl}`, err);
            }
          }
          console.log(`Successfully downloaded ${downloadedCount}/${fontUrls.length} fonts.`);
          resolve();
        } catch (e) {
          reject(e);
        }
      });
    }).on('error', reject);
  });
}

async function run() {
  console.log('Starting asset downloads...');
  for (const asset of assets) {
    try {
      await downloadFile(asset.url, asset.dest);
    } catch (err) {
      console.error(`Error downloading ${asset.url}:`, err.message);
    }
  }
  
  try {
    await fetchGoogleFonts();
  } catch (err) {
    console.error('Failed to fetch/download Google Fonts:', err);
  }
  
  console.log('All downloads completed!');
}

run();
