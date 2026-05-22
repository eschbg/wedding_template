import os
import glob
from PIL import Image

def optimize_image(filepath, max_width=1500):
    try:
        if filepath.endswith('.tif') or filepath.endswith('.tiff'):
            return # We will just delete tif files later
            
        file_ext = os.path.splitext(filepath)[1].lower()
        if file_ext == '.webp':
            return
            
        img = Image.open(filepath)
        
        # Convert RGBA to RGB for webp
        if img.mode in ('RGBA', 'P'):
            img = img.convert('RGB')
            
        # Resize if too large
        if img.width > max_width:
            ratio = max_width / float(img.width)
            new_height = int((float(img.height) * float(ratio)))
            img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
            
        # Save as webp
        out_path = os.path.splitext(filepath)[0] + '.webp'
        img.save(out_path, 'WEBP', quality=80)
        print(f"Optimized: {filepath} -> {out_path}")
        
    except Exception as e:
        print(f"Failed to optimize {filepath}: {e}")

# Target directories
dirs = ['public', 'src/assets/images']

for d in dirs:
    for ext in ('*.jpg', '*.jpeg', '*.png'):
        for f in glob.glob(os.path.join(d, ext)):
            # Only optimize files > 500KB to save time, or just optimize all?
            # We'll optimize all to ensure standard format.
            if "edited" in f:
                continue # Skip previously edited webp
            optimize_image(f)
