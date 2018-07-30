from PIL import Image,ImageOps
import sys

# arg1 = InputImagePath(Mandatory)
# arg2 = ImageBorderThickness
# arg3 = MaintainImageSize(boolean)
# arg4 = OutputImagePath(Default in Pictures)
# arg5 = AddDropShadow

# Setting Image Path
if(len(sys.argv) == 1):
    print("Expecting Image Path as argument")
else:
    img = Image.open(sys.argv[1])
    print("original size",img.size)
    img1 = ImageOps.expand(img,border=30,fill='white')
    img1.save("C:\\Users\\Public\\Pictures\\Sample Pictures\\new.jpg")
    print("Added Border",img1.size)
    # tempimg = ImageOps.crop(img,30)

    # img.thumbnail((964,708),Image.ANTIALIAS)
    # img.save("C:\\Users\\Public\\Pictures\\Sample Pictures\\thumb00.jpg")
    # tempimg = Image.open("C:\\Users\\Public\\Pictures\\Sample Pictures\\thumb00.jpg")
    # img2 = ImageOps.expand(tempimg,30,'white')
    # img2.save("C:\\Users\\Public\\Pictures\\Sample Pictures\\crop.jpg")
    # print("Cropped",img2.size)
# Image Border Thickness set  default if no argument is passed




