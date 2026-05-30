import re

with open("public/webcake-styles.css", "r", encoding="utf-8") as f:
    css = f.read()

matches = re.findall(r'@(?:-webkit-)?keyframes slideInDown\s*{[^}]+}', css)
if matches:
    print("Found slideInDown")
else:
    print("Not found slideInDown")
