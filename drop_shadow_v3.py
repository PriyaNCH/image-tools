from PIL import Image, ImageFilter

im = Image.open("C:\\Users\\Public\\Pictures\\Sample Pictures\\Tulips.jpg")
# shadow = Image.new(im.mode,(im.size[0],im.size[1]),"red")
# for i in range(0,10):
#     shadow = shadow.filter(ImageFilter.BLUR)
# shadow.show()\

im.filter(ImageFilter.BLUR).show()