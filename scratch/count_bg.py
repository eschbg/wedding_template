import urllib.request
import re

url = "https://www.thiepcuoikhanhan.click/QuocHuy-HaiYen"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        
    print("URL 1 count:", html.count("08/3f/7a/e9"))
    print("URL 2 count:", html.count("6a/ee/06/9e"))
    print("URL 3 count:", html.count("7c/ab/90/a0"))

except Exception as e:
    print(f"Error: {e}")
