import urllib.request
import re

url = "https://www.thiepcuoikhanhan.click/QuocHuy-HaiYen"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        
    print("Finding .section-background rules:")
    # Find all occurrences of .section-background { background: ... }
    matches = re.findall(r'\.section-background\s*\{\s*background.*?(url\([^)]+\))', html, re.DOTALL)
    for m in set(matches):
        print(m)
            
except Exception as e:
    print(f"Error: {e}")
