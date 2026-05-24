import urllib.request
import re

url = "https://www.thiepcuoikhanhan.click/QuocHuy-HaiYen"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        
    idx = html.find("16.05.2026")
    if idx != -1:
        # Search backward for 'w-builder-section'
        html_before = html[:idx]
        section_idx = html_before.rfind('w-builder-section')
        if section_idx != -1:
            # find the <div id="w-..." near here
            div_start = html_before.rfind('<div', 0, section_idx)
            div_tag = html[div_start:div_start+100]
            m = re.search(r'id="(w-[^"]+)"', div_tag)
            if m:
                sec_id = m.group(1)
                print(f"Found section ID: {sec_id}")
                
                # Now search for its background in styles
                styles = re.findall(rf'#{sec_id}\s*\.section-background\s*{{([^}}]+)}}', html)
                for s in styles:
                    print(f"Background: {s}")
                    
                # Search overlay
                overlays = re.findall(rf'#{sec_id}\s*\.section-overlay\s*{{([^}}]+)}}', html)
                for o in overlays:
                    print(f"Overlay: {o}")
                    
except Exception as e:
    print(f"Error: {e}")
