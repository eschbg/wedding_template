import re

with open("public/webcake-styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# Replace width, height, top, left in #w-gackq6hi .image-background
def replace_props(css_content):
    pattern = r'(#w-gackq6hi\s*\.image-background\s*{[^}]*?)width:\s*[^;]+;(\s*)height:\s*[^;]+;(\s*)top:\s*[^;]+;(\s*)left:\s*[^;]+;'
    repl = r'\1width: 202.71015624999998px;\2height: 314.7293799701789px;\3top: 0px;\4left: 0px;'
    
    # Wait, the order might not be strictly width, height, top, left.
    # It's safer to use re.sub for each property specifically within the block.
    return css_content

# Let's do it with a function
def fix_css_block(match):
    block = match.group(0)
    block = re.sub(r'width:\s*[^;]+;', 'width: 202.71015624999998px;', block)
    block = re.sub(r'height:\s*[^;]+;', 'height: 314.7293799701789px;', block)
    block = re.sub(r'top:\s*[^;]+;', 'top: 0px;', block)
    block = re.sub(r'left:\s*[^;]+;', 'left: 0px;', block)
    return block

css = re.sub(r'#w-gackq6hi\s*\.image-background\s*{[^}]+}', fix_css_block, css)

with open("public/webcake-styles.css", "w", encoding="utf-8") as f:
    f.write(css)

print("CSS updated successfully.")
