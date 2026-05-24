import re

with open("public/webcake-styles.css", "r", encoding="utf-8") as f:
    css = f.read()

matches = re.findall(r'#w-gackq6hi\s*\.image-background\s*{([^}]+)}', css)
for m in matches:
    print(m.strip())
