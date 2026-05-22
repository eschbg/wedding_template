import os
import glob

vue_files = glob.glob('src/**/*.vue', recursive=True)
for f in vue_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    new_content = content.replace('.jpg', '.webp').replace('.png', '.webp').replace('.jpeg', '.webp')
    
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Updated {f}")
