import urllib.request
import re

url = "https://www.thiepcuoikhanhan.click/QuocHuy-HaiYen"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        
    print("Found urls in background styles:")
    urls = re.findall(r'url\((.*?)\)', html)
    for u in set(urls):
        if 'png' in u or 'jpg' in u or 'webp' in u:
            print(u)
            
except Exception as e:
    print(f"Error: {e}")
