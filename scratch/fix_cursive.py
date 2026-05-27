import re

def fix_css(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        css = f.read()

    # Update #w-xlffzoii .text-block-css to cursive
    def repl_title_text(m):
        content = m.group(0)
        # Change font-family
        content = re.sub(r"font-family:\s*'[^']+',\s*sans-serif;", "font-family: 'thiep 6.ttf', sans-serif;", content)
        # Change font-size
        content = re.sub(r'font-size:\s*[\d.]+px;', 'font-size: 36px;', content)
        # Change line-height
        content = re.sub(r'line-height:\s*[\d.]+;', 'line-height: 1.2;', content)
        # Remove or change text-transform
        content = re.sub(r'text-transform:\s*uppercase;', 'text-transform: none;', content)
        return content

    css = re.sub(r'#w-xlffzoii \.text-block-css\s*\{[^}]*\}', repl_title_text, css)

    # Let's increase width of container to 400px to give it more room for cursive font
    def repl_title_box(m):
        content = m.group(0)
        content = re.sub(r'width:\s*[\d.]+px;', 'width: 420px;', content)
        content = re.sub(r'left:\s*[\d.]+px;', 'left: 0px;', content)
        return content

    css = re.sub(r'#w-xlffzoii\s*\{[^}]*\}', repl_title_box, css)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(css)

fix_css("public/webcake-styles.css")
fix_css("src/assets/original-webcake.css")
print("Changed title to cursive successfully.")
