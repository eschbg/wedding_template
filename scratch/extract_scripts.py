import re
from bs4 import BeautifulSoup

with open("public/original.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")
scripts = soup.find_all("script")
for s in scripts:
    content = s.string
    if content and 'animation' in content:
        print("--- Found script with animation ---")
        print(content[:500] + "...")
