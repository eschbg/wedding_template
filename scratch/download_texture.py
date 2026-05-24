import urllib.request

url = "https://content.pancake.vn/1/fwebp80/6a/ee/06/9e/dded87b0a266764c44e6f29502e2c94873a6eba5a00c2792903edc09-w:750-h:750-l:57152-t:image/jpeg.jpg"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        with open('scratch/texture.jpg', 'wb') as f:
            f.write(response.read())
    print("Downloaded texture")
except Exception as e:
    print(f"Error: {e}")
