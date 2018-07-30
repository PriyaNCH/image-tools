from PIL import Image

#Open the file and convert it to grey scale and save it. 
grey_img = Image.open('images/Desert.png').convert('L')
#Image not opened from a file has no format
print(grey_img.size,grey_img.format,grey_img.mode)
# grey_img.show()
new_grey_img = grey_img.save('images/Desert_grey.png')  #The save method returns nothings
new_grey_img.show()
print(new_grey_img.size,new_grey_img.format,new_grey_img.mode)


