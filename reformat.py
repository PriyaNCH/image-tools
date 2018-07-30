from PIL import Image
img = Image.open('C:/Users/Public/Pictures/Sample Pictures/Desert.jpg')
img.save('images/Desert.png')
print("firstimage",img.format)
img1 = Image.open('Desert.png')
print(img1.size)
print("secondimage",img1.format)