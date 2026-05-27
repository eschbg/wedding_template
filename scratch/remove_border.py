import re

def fix_css(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        css = f.read()

    # Remove border for photo 1 (#w-l6nufaq3)
    def repl_border_1(m):
        content = m.group(0)
        content = re.sub(r'border-width:\s*[\d.]+px;', 'border-width: 0px;', content)
        return content

    css = re.sub(r'#w-l6nufaq3 \.image-block-css\s*\{[^}]*\}', repl_border_1, css)

    # Remove border for photo 2 (#w-y4tq64wq)
    def repl_border_2(m):
        content = m.group(0)
        content = re.sub(r'border-width:\s*[\d.]+px;', 'border-width: 0px;', content)
        return content

    css = re.sub(r'#w-y4tq64wq \.image-block-css\s*\{[^}]*\}', repl_border_2, css)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(css)

fix_css("public/webcake-styles.css")
fix_css("src/assets/original-webcake.css")
print("Removed white border from photos successfully.")
