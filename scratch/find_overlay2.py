import urllib.request
import re

url = "https://www.thiepcuoikhanhan.click/QuocHuy-HaiYen"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        
    print("Finding rgba(77, 120, 164, 1) usage:")
    matches = re.findall(r'[^;{}]*rgba\(77, 120, 164, 1\)[^;{}]*', html)
    for m in matches:
        print(m)
        
except Exception as e:
    print(f"Error: {e}")
