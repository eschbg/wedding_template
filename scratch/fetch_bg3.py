import urllib.request
import re

url = "https://www.thiepcuoikhanhan.click/QuocHuy-HaiYen"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        
    print("Finding .section-background properties:")
    # Find all occurrences of .section-background { ... }
    matches = re.findall(r'\.section-background\s*\{([^}]+)\}', html, re.DOTALL)
    for m in set(matches):
        print(m.strip())
        print("---")
            
except Exception as e:
    print(f"Error: {e}")
