import urllib.request
import re

url = "https://www.thiepcuoikhanhan.click/QuocHuy-HaiYen"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        
    # Find Save The Date
    idx = html.find("Save The Date")
    if idx != -1:
        # Find the preceding <div id="w-..." class="w-builder-section">
        # Let's search backwards from idx
        text_before = html[:idx]
        matches = list(re.finditer(r'<div\s+id="([^"]+)"\s+class="[^"]*w-builder-section[^"]*"', text_before))
        if matches:
            last_match = matches[-1]
            section_id = last_match.group(1)
            print(f"Section ID containing Save The Date: {section_id}")
            
            # Now find the background style for this section in the HTML
            style_matches = re.findall(rf'#{section_id}\s*\.section-background\s*{{([^}}]+)}}', html)
            for s in style_matches:
                print(f"Section background: {s}")
                
            overlay_matches = re.findall(rf'#{section_id}\s*\.section-overlay\s*{{([^}}]+)}}', html)
            for o in overlay_matches:
                print(f"Section overlay: {o}")

except Exception as e:
    print(f"Error: {e}")
