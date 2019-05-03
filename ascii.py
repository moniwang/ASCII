import PIL
from PIL import Image
import numpy as np
import sys

img = Image.open(sys.argv[1])
width, height = img.size
if width > 500 or height > 500:
    img = img.resize((round(width/max(width,height)*500), round(height/max(width,height)*500)))

width, height = img.size
pixels = img.load()
rgb_img = img.convert('RGB')

# chars = " '^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
# chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1\{\}[]?-_+~<>i!lI;:,\"^`'. "
chars = " .:-=+*#%@"
chars = " .+#@"
for j in range(height):
    for i in range(width):
        r, g, b = rgb_img.getpixel((i,j))
        lumo = round(0.21*r + 0.72*g + 0.07*b)
        #lumo = (r+g+b)/3
        #lumo = (max(r, g, b) + min(r, g , b))/2
        lumo = round((lumo/255)*4)
        for k in range(3):
            print(chars[-(lumo+1)], end="")
    print("")