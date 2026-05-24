import urllib.request
import re

url = "https://www.thiepcuoikhanhan.click/QuocHuy-HaiYen"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        
    print("Finding section specific overlays:")
    # Look for .section-overlay styles
    matches = re.findall(r'(#[a-zA-Z0-9_-]+)\s*\.section-overlay\s*\{([^}]+)\}', html)
    for m in matches:
        print(f"Section {m[0]} overlay: {m[1].strip()}")
        
    print("\nFinding section background colors:")
    matches = re.findall(r'(#[a-zA-Z0-9_-]+)\s*\.section-background\s*\{([^}]+)\}', html)
    for m in matches:
        if 'background-color' in m[1] or 'rgba' in m[1] or '#' in m[1]:
            print(f"Section {m[0]} bg: {m[1].strip()}")
            
except Exception as e:
    print(f"Error: {e}")
