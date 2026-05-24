import urllib.request
import re

url = "https://www.thiepcuoikhanhan.click/QuocHuy-HaiYen"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        
    print("Finding rgba(6,21,40,.05) element:")
    
    # We want to find the CSS selector for this color.
    # It might be in a <style> tag.
    matches = re.findall(r'([^}{]+)\s*\{[^}]*rgba\(6,21,40,\.05\)[^}]*\}', html)
    for m in matches:
        print(f"Selector: {m.strip()}")
        
except Exception as e:
    print(f"Error: {e}")
