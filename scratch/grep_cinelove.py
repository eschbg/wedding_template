with open(r"C:\Users\ADMIN\.gemini\antigravity\brain\62284b45-c1d2-4f7a-b01f-c564c45daec6\.system_generated\steps\1153\content.md", "r", encoding="utf-8") as f:
    text = f.read()

import re
matches = re.finditer(r'.{0,50}lời nhắn.{0,50}', text, re.IGNORECASE)
for m in matches:
    print(m.group(0))

matches2 = re.finditer(r'.{0,50}lời chúc.{0,50}', text, re.IGNORECASE)
for m in matches2:
    print(m.group(0))
