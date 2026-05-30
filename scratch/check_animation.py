import re

with open("public/webcake-styles.css", "r", encoding="utf-8") as f:
    css = f.read()

matches = re.findall(r'#[a-zA-Z0-9-]+\.animation\s*{[^}]+}', css)
if matches:
    print(matches[0])
    print("Found {} matches".format(len(matches)))
else:
    print("No matches for #[id].animation")
