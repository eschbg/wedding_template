import urllib.request
import re
from bs4 import BeautifulSoup

url = "https://www.thiepcuoikhanhan.click/QuocHuy-HaiYen"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        
    soup = BeautifulSoup(html, 'html.parser')
    
    # Check styles for background colors that might be bluish
    # e.g., rgba(..., 0.something) or hex codes
    for style in soup.find_all('style'):
        text = style.text
        # Find all background: #... or background-color: #...
        colors = set(re.findall(r'background(?:-color)?:\s*(#[0-9a-fA-F]{3,8}|rgba\([^)]+\))', text))
        for c in colors:
            print("Found color:", c)
            
except Exception as e:
    print(f"Error: {e}")
