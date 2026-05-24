import urllib.request
import re

url = "https://www.thiepcuoikhanhan.click/QuocHuy-HaiYen"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        
    print("Finding Quý Khách")
    # let's just find the index and print surrounding context
    idx = html.find("Quý Khách")
    if idx != -1:
        print("Found 'Quý Khách'!")
    else:
        print("Not found 'Quý Khách'")
        
    idx2 = html.find("16.05.2026")
    if idx2 != -1:
        print("Found '16.05.2026'!")
        start = max(0, idx2 - 500)
        end = min(len(html), idx2 + 500)
        print("Context:")
        print(html[start:end])
    else:
        print("Not found '16.05.2026'")
        
except Exception as e:
    print(f"Error: {e}")
