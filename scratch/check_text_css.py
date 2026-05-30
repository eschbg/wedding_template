import re

with open("public/webcake-styles.css", "r", encoding="utf-8") as f:
    css = f.read()

def print_css(el_id):
    print(f"--- {el_id} ---")
    matches = re.findall(rf'(#{el_id}\s*{{[^}}]+}})', css)
    for m in matches:
        print(m.strip())

print_css("w-jkdnlfq9")
print_css("w-2je4g75n")
