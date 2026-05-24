import urllib.request
from PIL import Image
import io

urls = [
    "https://content.pancake.vn/1/08/3f/7a/e9/be9a053a77ec7cdb461246a62779525962247b7146d4dcccce9c1cfb.png",
    "https://content.pancake.vn/1/fwebp80/6a/ee/06/9e/dded87b0a266764c44e6f29502e2c94873a6eba5a00c2792903edc09-w:750-h:750-l:57152-t:image/jpeg.jpg",
    "https://content.pancake.vn/web-media-262/s840x1260/fwebp80/7c/ab/90/a0/7effe9cabaebe1e81ff72f1f792a048deffb902a566e885da80b0d6c-w:1707-h:2560-l:232508-t:image/jpeg.jpg"
]

for url in urls:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        response = urllib.request.urlopen(req)
        img_data = response.read()
        img = Image.open(io.BytesIO(img_data)).convert('RGB')
        
        # Calculate average color
        r_total, g_total, b_total = 0, 0, 0
        pixels = list(img.getdata())
        for pixel in pixels:
            r_total += pixel[0]
            g_total += pixel[1]
            b_total += pixel[2]
            
        num_pixels = len(pixels)
        r_avg = r_total // num_pixels
        g_avg = g_total // num_pixels
        b_avg = b_total // num_pixels
        
        print(f"URL: {url}")
        print(f"Average Color (RGB): ({r_avg}, {g_avg}, {b_avg})")
        print("---")
            
    except Exception as e:
        print(f"Error for {url}: {e}")
