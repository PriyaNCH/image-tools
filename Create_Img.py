from PIL import Image

# im = Image.new("RGBA",(1024,1024),"black")
im = Image.new("L",(512,512))
im.show()
print(im.size)

# Refer on modes 
# http://svn.effbot.org/public/tags/pil-1.1.4/libImaging/Unpack.c
# http://effbot.org/imagingbook/decoder.htm