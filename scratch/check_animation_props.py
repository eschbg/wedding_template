import re

with open("public/webcake-styles.css", "r", encoding="utf-8") as f:
    css = f.read()

def print_css(el_id):
    print(f"--- {el_id} ---")
    matches = re.findall(rf'(#{el_id}\.animation\s*{{[^}}]+}})', css)
    for m in matches:
        print(m.strip())
    matches2 = re.findall(rf'(#{el_id}\.animation\s*\.[a-zA-Z0-9-]+\s*{{[^}}]+}})', css)
    for m in matches2:
        print(m.strip())

print_css("w-4onqz968")
