from PIL import Image
from random import randint

img = Image.new("RGB", (1920,1080), color = 'black')

def check_inside(x,y):
    a = 800
    b = 400
    if (x-960)**2/a**2 + (y-540)**2/b**2 <= 1:
        return True
    return False

pixels = img.load()
for i in range(1920):
    for j in range(1080):
        
        if check_inside(i,j):
            pixels[i,j] = (randint(0,255),randint(0,255),randint(0,255))

img = img.save("transluminal.jpg")


