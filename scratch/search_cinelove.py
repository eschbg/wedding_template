import re
from bs4 import BeautifulSoup

with open(r"C:\Users\ADMIN\.gemini\antigravity\brain\62284b45-c1d2-4f7a-b01f-c564c45daec6\.system_generated\steps\1153\content.md", "r", encoding="utf-8") as f:
    text = f.read()

soup = BeautifulSoup(text, 'html.parser')
for text_node in soup.stripped_strings:
    t = text_node.lower()
    if 'ẩn' in t or 'hiện' in t or 'chúc' in t or 'nhắn' in t:
        print(text_node)
