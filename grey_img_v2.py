from PIL import Image

'''Saving the file immediately after opening and converting'''
Image.open('images/Desert.png').convert('L').save('images/Desert_grey.png')
new_grey_img = Image.open('images/Desert_grey.png')  #The save method returns nothings
new_grey_img.show()
print(new_grey_img.size,new_grey_img.format,new_grey_img.mode)


