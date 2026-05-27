import re

def fix_css(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        css = f.read()

    # 1. Update font-size to 42px
    def repl_title_text(m):
        content = m.group(0)
        content = re.sub(r'font-size:\s*[\d.]+px;', 'font-size: 42px;', content)
        return content

    css = re.sub(r'#w-xlffzoii \.text-block-css\s*\{[^}]*\}', repl_title_text, css)

    # 2. Shift date and photos down by 40px
    def shift_top(css_content, el_id, shift_amount):
        pattern = rf'(#{el_id}\s*{{[^}}]*?top:\s*)([-0-9.]+)px'
        def repl(m):
            new_val = float(m.group(2)) + shift_amount
            return m.group(1) + str(new_val) + "px"
        return re.sub(pattern, repl, css_content)

    css = shift_top(css, "w-2je4g75n", 40)
    css = shift_top(css, "w-l6nufaq3", 40)
    css = shift_top(css, "w-8ay25ugn", 40)
    css = shift_top(css, "w-y4tq64wq", 40)
    css = shift_top(css, "w-yt01nt06", 40)
    css = shift_top(css, "w-5q0v20ee", 40)

    # also shift the section height so it doesn't get cut off
    def shift_height(css_content, el_id, shift_amount):
        pattern = rf'(#{el_id}\s*{{[^}}]*?height:\s*)([-0-9.]+)px'
        def repl(m):
            new_val = float(m.group(2)) + shift_amount
            return m.group(1) + str(new_val) + "px"
        return re.sub(pattern, repl, css_content)
    
    css = shift_height(css, "w-vd7mc3fa", 40)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(css)

fix_css("public/webcake-styles.css")
fix_css("src/assets/original-webcake.css")
print("Aligned again successfully.")
