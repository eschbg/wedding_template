import re
import urllib.request
import urllib.error
import time

with open("public/webcake-styles.css", "r", encoding="utf-8") as f:
    css = f.read()

urls = re.findall(r'url\("?(https://[^\)"]+)"?\)', css)
unique_urls = list(set(urls))
print(f"Found {len(unique_urls)} unique URLs.")

total_size = 0
for url in unique_urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req)
        size = int(response.headers.get('Content-Length', 0))
        total_size += size
        if size > 500000: # 500 KB
            print(f"LARGE IMAGE: {size / 1024 / 1024:.2f} MB - {url}")
    except Exception as e:
        print(f"Error for {url}: {e}")
    time.sleep(0.1)

print(f"Total size: {total_size / 1024 / 1024:.2f} MB")
