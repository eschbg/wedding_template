import os
from PIL import Image

pngs = [
    'src/assets/images/countdown-bg.png',
    'src/assets/images/countdown-flower.png',
    'src/assets/images/gate-left.png',
    'src/assets/images/gate-right.png',
    'src/assets/images/music-disc.png',
    'src/assets/images/qr-cr.png',
    'src/assets/images/rsvp-bg.png',
    'src/assets/images/thank-you-bg.png'
]

for filepath in pngs:
    try:
        img = Image.open(filepath)
        
        # Resize if too large
        max_width = 1500
        if img.width > max_width:
            ratio = max_width / float(img.width)
            new_height = int((float(img.height) * float(ratio)))
            img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
            
        # Save as webp WITHOUT converting to RGB, preserving RGBA
        out_path = os.path.splitext(filepath)[0] + '.webp'
        # WebP supports RGBA natively
        img.save(out_path, 'WEBP', quality=80)
        print(f"Fixed and optimized: {filepath} -> {out_path}")
        
    except Exception as e:
        print(f"Failed to optimize {filepath}: {e}")
