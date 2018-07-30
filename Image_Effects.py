from PIL import Image,ImageOps
import sys, argparse, os, random, string

def filename_generator():
    return ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for _ in range(5))
from PIL import Image,ImageFilter

def makeShadow(image, iterations, border, offset, backgroundColour, shadowColour):
    # image: base image to give a drop shadow
    # iterations: number of times to apply the blur filter to the shadow
    # border: border to give the image to leave space for the shadow
    # offset: offset of the shadow as [x,y]
    # backgroundCOlour: colour of the background
    # shadowColour: colour of the drop shadow
    
    #Calculate the size of the shadow's image
    fullWidth  = image.size[0] + abs(offset[0]) + 2*border
    fullHeight = image.size[1] + abs(offset[1]) + 2*border
    
    #Create the shadow's image. Match the parent image's mode.
    shadow = Image.new(image.mode, (fullWidth, fullHeight), backgroundColour)
    
    # Place the shadow, with the required offset
    shadowLeft = border + max(offset[0], 0) #if <0, push the rest of the image right
    shadowTop  = border + max(offset[1], 0) #if <0, push the rest of the image down
    #Paste in the constant colour
    shadow.paste(shadowColour, 
                [shadowLeft, shadowTop,
                 shadowLeft + image.size[0],
                 shadowTop  + image.size[1] ])
    
    # Apply the BLUR filter repeatedly
    for i in range(iterations):
        shadow = shadow.filter(ImageFilter.BLUR)

    # Paste the original image on top of the shadow 
    imgLeft = border - min(offset[0], 0) #if the shadow offset was <0, push right
    imgTop  = border - min(offset[1], 0) #if the shadow offset was <0, push down
    shadow.paste(image, (imgLeft, imgTop))

    return shadow

parser = argparse.ArgumentParser('Read from command line')
parser.add_argument("in_image_path",help="Give the input image directory path")
parser.add_argument("--output","--out_image_path",help="Give the path to save edited image",default="C:\\Users\\Public\\Pictures\\"+filename_generator()+".png")
parser.add_argument("--border","--image_border",help="Give the image border thickness",type=int,default=10)
parser.add_argument("--border_fill","--image_border_fill",help="Give the image border fill color",default='white')
parser.add_argument("--shadow","--add_drop_shadow",help="Want Drop Shadow effect?",type=bool)
args = parser.parse_args()

# Verify input file path
if not os.path.isfile(args.in_image_path):
    print(args.in_image_path,"is not a valid file or file name is missing in the path")

img = Image.open(args.in_image_path)

# Edit the image based on drop shadow effect 
if args.shadow:
    image_edited = makeShadow(img,5,20,[20,20],"white","black")
else:
    image_edited = ImageOps.expand(img,border=abs(args.border),fill=args.border_fill)

image_edited.save(args.output)
print("Image is saved at",args.output)

resp = input("Display the edited image-Y/N?   ")
if resp == 'Y' or resp == 'y':
    disp_img = Image.open(args.output)
    disp_img.show()
else:
    exit