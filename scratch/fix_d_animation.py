import re

with open("public/webcake-styles.css", "r", encoding="utf-8") as f:
    css = f.read()

replacement = r'''\1
      animation-name: slideInUp;
      -webkit-animation-name: slideInUp;
      animation-delay: 0s;
      -webkit-animation-delay: 0s;
      animation-iteration-count: 1;
      -webkit-animation-iteration-count: 1;
      animation-duration: 1s;
      -webkit-animation-duration: 1s;'''

# Find the block and replace it
css = re.sub(r'(#w-06fskfrb\.animation\s*\.text-block-css\s*{)', replacement, css)

with open("public/webcake-styles.css", "w", encoding="utf-8") as f:
    f.write(css)

print("CSS updated successfully.")
