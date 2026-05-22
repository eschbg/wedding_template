import os
import glob

dirs = ['public', 'src/assets/images']
for d in dirs:
    # Delete all tif
    for f in glob.glob(os.path.join(d, '*.tif*')):
        os.remove(f)
        print(f"Deleted {f}")
        
    # Delete jpg/png if a webp exists
    for ext in ('*.jpg', '*.jpeg', '*.png'):
        for f in glob.glob(os.path.join(d, ext)):
            webp_path = os.path.splitext(f)[0] + '.webp'
            if os.path.exists(webp_path):
                os.remove(f)
                print(f"Deleted {f}")
