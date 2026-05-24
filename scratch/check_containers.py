import re

with open("public/webcake-styles.css", "r", encoding="utf-8") as f:
    css = f.read()

def get_css(el_id):
    print(f"--- {el_id} ---")
    matches = re.findall(rf'(#{el_id}\s*{{[^}}]+}})', css)
    for m in matches:
        print(m.strip())

get_css("w-gackq6hi")
get_css("w-l628a6sl")
