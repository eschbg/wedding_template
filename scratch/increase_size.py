import re

def fix_css(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        css = f.read()

    # Update #w-xlffzoii .text-block-css font size
    def repl_title_text(m):
        content = m.group(0)
        # Change font-size to 55px
        content = re.sub(r'font-size:\s*[\d.]+px;', 'font-size: 55px;', content)
        return content

    css = re.sub(r'#w-xlffzoii \.text-block-css\s*\{[^}]*\}', repl_title_text, css)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(css)

fix_css("public/webcake-styles.css")
fix_css("src/assets/original-webcake.css")
print("Increased quote font size successfully.")
