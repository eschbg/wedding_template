import re

with open("public/webcake-styles.css", "r", encoding="utf-8") as f:
    css = f.read()

def shift_top(css_content, el_id, shift_amount):
    pattern = rf'(#{el_id}\s*{{[^}}]*?top:\s*)([0-9.]+)px'
    def repl(m):
        new_val = float(m.group(2)) - shift_amount
        return m.group(1) + str(new_val) + "px"
    return re.sub(pattern, repl, css_content)

def change_height(css_content, el_id, reduce_amount):
    pattern = rf'(#{el_id}\s*{{[^}}]*?height:\s*)([0-9.]+)px'
    def repl(m):
        new_val = float(m.group(2)) - reduce_amount
        return m.group(1) + str(new_val) + "px"
    return re.sub(pattern, repl, css_content)

shift = 60
css = shift_top(css, "w-qa4iudj9", shift)
css = shift_top(css, "w-xlffzoii", shift)
css = shift_top(css, "w-2je4g75n", shift)
css = shift_top(css, "w-l6nufaq3", shift)
css = shift_top(css, "w-y4tq64wq", shift)
css = shift_top(css, "w-yt01nt06", shift)
css = shift_top(css, "w-5q0v20ee", shift)

css = change_height(css, "w-vd7mc3fa", shift)

with open("public/webcake-styles.css", "w", encoding="utf-8") as f:
    f.write(css)

print("CSS updated successfully.")
