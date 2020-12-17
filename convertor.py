from PIL import Image 
import PIL
import os
PIL.Image.MAX_IMAGE_PIXELS = 4000000000

for filename in os.listdir("./input"):
    print(filename)
    im = Image.open("./input/"+filename) 
    width, height = im.size
    print(width, height) 
  
    for H in range(int(height/1024)):
        for W in range(int(width/1024)):
            left = W*1024
            right = (W+1)*1024
            top = H*1024
            bottom = (H+1)*1024
            im1 = im.crop((left, top, right, bottom)) 
            im1.save("./output/test" + filename.split(".")[0] + "{}{}.png".format(H,W), format="PNG")
  
