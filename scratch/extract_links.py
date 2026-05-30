from bs4 import BeautifulSoup

with open("public/original.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")
for link in soup.find_all("link"):
    print("Link:", link.get("href"))

for style in soup.find_all("style"):
    content = style.string
    if content and "@keyframes" in content:
        print("Found keyframes in style tag")
