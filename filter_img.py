from PIL import Image,ImageFilter

print(dir(Image))
Image_Path = 'resources/Images/'
img = Image.open('resources/Images/Desert.jpg')
# img.show()

#Emboss the image
im_sharpen = img.filter(ImageFilter.SHARPEN)
im_blur = img.filter(ImageFilter.BLUR)
im_edg  = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
im_contour = img.filter(ImageFilter.CONTOUR)    

im_sharpen.save(Image_Path+'Desert_sharpen.jpg')
im_blur.save(Image_Path+'Desert_blur.jpg')
im_edg.save(Image_Path+'Desert_edg.jpg')
im_contour.save(Image_Path+'Desert_contr.jpg')

#Split the image into respective bands R,G,B
r,g,b = im_sharpen.split()
print('r band',r,'g band',g,'b band',b)

#View EXIF data embedded in an image 
#EXIF Data -> Exchangeable Image File format
#EXIF Data ->  ISO speed, shutter speed, aperture, white balance, camera model and make, date and time, lens type, focal length etc.
exif_data = img._getexif()
print(exif_data)