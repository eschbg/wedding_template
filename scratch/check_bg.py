import re

with open("public/webcake-styles.css", "r", encoding="utf-8") as f:
    css = f.read()

print("--- body ---")
matches = re.findall(r'(body\s*{[^}]+})', css)
for m in matches: print(m.strip())

print("--- .section-background ---")
matches = re.findall(r'(\.section-background\s*{[^}]+})', css)
for m in matches: print(m.strip())

print("--- .pageview ---")
matches = re.findall(r'(\.pageview\s*{[^}]+})', css)
for m in matches: print(m.strip())

print("--- .overlay ---")
matches = re.findall(r'(\.overlay\s*{[^}]+})', css)
for m in matches: print(m.strip())
