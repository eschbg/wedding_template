import urllib.request
from bs4 import BeautifulSoup
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

url = "https://www.thiepcuoikhanhan.click/QuocHuy-HaiYen"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        
    soup = BeautifulSoup(html, 'html.parser')
    
    # Let's find the section with "Save The Date"
    # We will search for all elements with "Save The Date"
    target_elements = soup.find_all(string=re.compile("Save The Date", re.IGNORECASE))
    
    for el in target_elements:
        # traverse up to find section
        curr = el.parent
        section = None
        while curr and curr.name != 'body':
            if curr.get('class') and 'w-builder-section' in curr.get('class'):
                section = curr
                break
            curr = curr.parent
            
        if section:
            print(f"--- FOUND SECTION --- ID: {section.get('id')} Classes: {section.get('class')}")
            # print all inline styles of section
            print(f"Section style: {section.get('style')}")
            
            # find all section-background
            bgs = section.find_all(class_='section-background')
            for bg in bgs:
                print(f".section-background style: {bg.get('style')}")
                
            # find all section-overlay
            overlays = section.find_all(class_='section-overlay')
            for ov in overlays:
                print(f".section-overlay style: {ov.get('style')}")
                
            print("-----------------------")
            
except Exception as e:
    print(f"Error: {e}")
