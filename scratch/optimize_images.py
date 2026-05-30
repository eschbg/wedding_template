import re
import urllib.request
import os
from PIL import Image
import hashlib

# Ensure directories exist
os.makedirs("public/cdn-images", exist_ok=True)
os.makedirs("public/images", exist_ok=True)

with open("public/webcake-styles.css", "r", encoding="utf-8") as f:
    css = f.read()

urls = list(set(re.findall(r'url\("?(https://[^\)"]+)"?\)', css)))
print(f"Found {len(urls)} unique CDN URLs to optimize.")

url_mapping = {}

for i, url in enumerate(urls):
    if not ("pancake.vn" in url):
        continue
    
    # Generate unique filename
    ext = ".png" if ".png" in url.lower() else ".jpg"
    hash_name = hashlib.md5(url.encode()).hexdigest()[:10]
    local_name = f"opt_{hash_name}{ext}"
    local_path = os.path.join("public/cdn-images", local_name)
    webp_name = f"opt_{hash_name}.webp"
    webp_path = os.path.join("public/images", webp_name)
    
    url_mapping[url] = f"/images/{webp_name}"
    
    if not os.path.exists(webp_path):
        print(f"[{i+1}/{len(urls)}] Downloading {url[:50]}...")
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response, open(local_path, 'wb') as out_file:
                out_file.write(response.read())
            
            # Convert and compress
            print(f"[{i+1}/{len(urls)}] Converting to WebP...")
            with Image.open(local_path) as img:
                # Resize if it's too huge, max width 1920
                if img.width > 1920:
                    ratio = 1920 / img.width
                    new_size = (1920, int(img.height * ratio))
                    img = img.resize(new_size, Image.Resampling.LANCZOS)
                
                # Convert to RGB if necessary for WebP (e.g. RGBA for JPEG? wait, WebP supports RGBA)
                if img.mode not in ('RGB', 'RGBA'):
                    img = img.convert('RGB')
                    
                img.save(webp_path, 'webp', quality=60, method=4)
        except Exception as e:
            print(f"Error processing {url}: {e}")
            url_mapping.pop(url, None)

# Update CSS
for old_url, new_url in url_mapping.items():
    # Replace the url literally
    css = css.replace(f'"{old_url}"', f'"{new_url}"')
    css = css.replace(f'url({old_url})', f'url("{new_url}")')

with open("public/webcake-styles.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Finished optimizing images and updated CSS!")
