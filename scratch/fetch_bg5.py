import urllib.request
import re

url = "https://www.thiepcuoikhanhan.click/QuocHuy-HaiYen"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        
    print("Finding .section-overlay properties:")
    # Find all occurrences of .section-overlay { ... }
    matches = re.findall(r'\.section-overlay\s*\{([^}]+)\}', html, re.DOTALL)
    for m in set(matches):
        print(m.strip())
        print("---")
        
    print("Finding solid background colors:")
    colors = set(re.findall(r'background(?:-color)?:\s*(#[0-9a-fA-F]{3,8}|rgba\([^)]+\))', html))
    for c in colors:
        print("Found color:", c)
            
except Exception as e:
    print(f"Error: {e}")
