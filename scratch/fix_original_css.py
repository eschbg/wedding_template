import re

data = open('src/assets/original-webcake.css', encoding='utf-8').read()

# Fix #w-l6nufaq3 .image-background
data = data.replace(
    '    #w-l6nufaq3 .image-background {\n      width: 180.27645502645504px;\n      height: 279px;\n      top: -29px;\n      left: 0px;',
    '    #w-l6nufaq3 .image-background {\n      width: 197px;\n      height: 266px;\n      top: 0px;\n      left: 0px;'
)

# Fix #w-y4tq64wq .image-background
data = re.sub(
    r'(#w-y4tq64wq \.image-background \{)\s*\n\s*width: 181\.[\d]+px;\s*\n\s*height: 280\.[\d]+px;\s*\n\s*top: -17\.[\d]+px;\s*\n\s*left: 0px;',
    r'\1\n      width: 197px;\n      height: 266px;\n      top: 0px;\n      left: 0px;',
    data
)

open('src/assets/original-webcake.css', 'w', encoding='utf-8').write(data)
print('Done fixing original-webcake.css!')
