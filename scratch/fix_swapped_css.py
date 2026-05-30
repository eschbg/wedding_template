import re

with open("public/webcake-styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# Replace #w-2je4g75n override with #w-jkdnlfq9
css = re.sub(
    r'#w-2je4g75n\s*{\s*left:\s*0\s*!important;\s*width:\s*420px\s*!important;\s*white-space:\s*nowrap\s*!important;\s*}',
    r'#w-jkdnlfq9 { left: 0 !important; width: 420px !important; white-space: nowrap !important; }',
    css
)

with open("public/webcake-styles.css", "w", encoding="utf-8") as f:
    f.write(css)

print("CSS updated successfully.")
