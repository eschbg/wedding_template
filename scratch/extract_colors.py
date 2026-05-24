import urllib.request
import re

url = "https://www.thiepcuoikhanhan.click/QuocHuy-HaiYen"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        
    print("Finding body/global background:")
    # look for body { ... } or .w-builder-body
    body_match = re.search(r'body\s*\{([^}]+)\}', html)
    if body_match:
        print(f"body: {body_match.group(1)}")
    
    body2 = re.search(r'\.w-builder-body\s*\{([^}]+)\}', html)
    if body2:
        print(f".w-builder-body: {body2.group(1)}")
        
    print("\nFinding all hex colors in styles:")
    styles = re.findall(r'<style[^>]*>(.*?)</style>', html, re.DOTALL)
    all_colors = set()
    for s in styles:
        # find hex colors
        hexes = re.findall(r'#[0-9a-fA-F]{6}', s)
        for h in hexes:
            all_colors.add(h.lower())
            
    for c in all_colors:
        print(f"Found hex: {c}")

except Exception as e:
    print(f"Error: {e}")
