from PIL import Image
import os
from pathlib import Path

imglist = Path('./images').glob('*dp')

for img in imglist:

    im=Image.open(img)
    
    # to get the image name from its whole path:
    filename = os.path.basename(img)
    ## to replace a string:
    # new_ext = filename.replace(".tiff", ".jpg") 
    im.rotate(90).resize((128,128)).convert("RGB").save("./img/"+filename+".jpg")

print("Images converted successfully")
