import urllib.request
url = "https://docs.google.com/spreadsheets/d/1qLyN6E3APjHWTShALFNqDBAlrF6Fz_2vxpDw0DcIS1A/export?format=csv&gid=0"
try:
    with urllib.request.urlopen(url) as response:
        html = response.read()
        with open("scratch/sheet.csv", "wb") as f:
            f.write(html)
        print("Saved to scratch/sheet.csv")
except Exception as e:
    print(f"Error: {e}")
