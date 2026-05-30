import re

with open("public/webcake-styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# Replace the specific background color and blend mode
css = re.sub(
    r'background-color:\s*rgba\(0,\s*50,\s*100,\s*0\.01\);',
    r'background-color: #ffffff;',
    css
)

with open("public/webcake-styles.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Background color updated to white.")
