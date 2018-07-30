"""This script creates thumbnails out of the images passed"""
import os
from PIL import Image

# make subfolder
NEWDIR = '../thumb300'
if not os.path.exists(NEWDIR):
    os.makedirs(NEWDIR)

# thumbnail size as tuple
THUMB_SIZE = (300, 300)

FILES = [f for f in os.listdir('../Images') if os.path.isfile("../Images/"+f)]
for f in FILES:
    name = '.'.join(f.split('.')[:-1])
    # ext = f.split('.')[-1]
    print(f.format)
    exit

#    # jpg only
#     filepath = "../Images/"+f
#     # if ext == 'jpg':
#     if ext == 'JPEG'
#         newname = name + '_300' + '.' + ext
#         image = Image.open(filepath)
#         image.thumbnail(THUMB_SIZE)
#         image.save(os.path.join(NEWDIR, newname))
# print("done")

