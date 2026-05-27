import re

def fix_css(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        css = f.read()

    # 1. Update #w-xlffzoii width, left, height
    def repl_title_box(m):
        content = m.group(0)
        content = re.sub(r'width:\s*[\d.]+px;', 'width: 380px;', content)
        content = re.sub(r'left:\s*[\d.]+px;', 'left: 20px;', content)
        content = re.sub(r'height:\s*[\d.]+px;', 'height: auto;', content)
        return content

    css = re.sub(r'#w-xlffzoii\s*\{[^}]*\}', repl_title_box, css)

    # 2. Update #w-xlffzoii .text-block-css font-size
    def repl_title_text(m):
        content = m.group(0)
        content = re.sub(r'font-size:\s*[\d.]+px;', 'font-size: 24px;', content)
        content = re.sub(r'line-height:\s*[\d.]+;', 'line-height: 1.4;', content)
        return content

    css = re.sub(r'#w-xlffzoii \.text-block-css\s*\{[^}]*\}', repl_title_text, css)

    # 3. Shift #w-2je4g75n top down by 40px
    def repl_date_box(m):
        content = m.group(0)
        def shift_top(m_top):
            new_top = float(m_top.group(1)) + 40
            return f"top: {new_top}px;"
        content = re.sub(r'top:\s*([\d.]+)px;', shift_top, content)
        return content

    css = re.sub(r'#w-2je4g75n\s*\{[^}]*\}', repl_date_box, css)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(css)

fix_css("public/webcake-styles.css")
fix_css("src/assets/original-webcake.css")
print("Fixed title CSS successfully.")
