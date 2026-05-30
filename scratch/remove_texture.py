import re

with open("public/webcake-styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# Replace the background url and blend mode with just the background color
css = re.sub(
    r'background:\s*center\s*center/\s*cover\s*no-repeat\s*content-box\s*border-box\s*url\("[^"]+"\);\s*background-color:\s*#ffffff;\s*background-blend-mode:\s*multiply;',
    r'background-color: #ffffff;',
    css
)

with open("public/webcake-styles.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Background texture removed, kept solid white color.")
