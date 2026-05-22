import os
import glob
import re

vue_files = glob.glob('src/**/*.vue', recursive=True)
for f in vue_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Simple regex to add loading="lazy" if not present in <img ...>
    # We'll skip <img that already has loading="lazy"
    def add_lazy(match):
        img_tag = match.group(0)
        if 'loading="lazy"' not in img_tag:
            return img_tag.replace('<img ', '<img loading="lazy" ')
        return img_tag
        
    new_content = re.sub(r'<img\s+[^>]*>', add_lazy, content)
    
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Added lazy loading to {f}")
