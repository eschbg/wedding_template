import re

with open("public/webcake-styles.css", "r", encoding="utf-8") as f:
    css = f.read()

ids = [
    "w-xnhxst1e",
    "w-gackq6hi",
    "w-l628a6sl"
]

for el_id in ids:
    print(f"--- {el_id} ---")
    matches = re.findall(rf'#{el_id}\s+\.image-background\s*{{[^}}]*?url\("([^"]+)"\)', css)
    if not matches:
        matches = re.findall(rf'#{el_id}\s*{{[^}}]*?url\("([^"]+)"\)', css)
    for m in matches:
        print(m)
