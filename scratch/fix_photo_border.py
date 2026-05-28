import re

data = open('public/webcake-styles.css', encoding='utf-8').read()

# Fix #w-l6nufaq3 .image-background - container is 197x266, image is 180x279
# Image is NARROWER than container -> white gap on right side
# Solution: make image fill container width
data = data.replace(
    '    #w-l6nufaq3 .image-background {\n      width: 180.27645502645504px;\n      height: 279px;\n      top: -29px;\n      left: 0px;',
    '    #w-l6nufaq3 .image-background {\n      width: 197px;\n      height: 266px;\n      top: 0px;\n      left: 0px;'
)

# Fix #w-y4tq64wq .image-background - container is 197x266, image is 181x280
data = re.sub(
    r'(#w-y4tq64wq \.image-background \{)\s*\n\s*width: 181\.[\d]+px;\s*\n\s*height: 280\.[\d]+px;\s*\n\s*top: -17\.[\d]+px;\s*\n\s*left: 0px;',
    r'\1\n      width: 197px;\n      height: 266px;\n      top: 0px;\n      left: 0px;',
    data
)

open('public/webcake-styles.css', 'w', encoding='utf-8').write(data)

# Verify
result = re.findall(r'#w-l6nufaq3 .image-background \{[^}]+\}', data)
for r in result:
    print(r)
print('---')
result2 = re.findall(r'#w-y4tq64wq .image-background \{[^}]+\}', data)
for r in result2:
    print(r)
print('Done!')
