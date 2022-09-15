from PIL import Image
import os

size = 512
basewidth =  512

def resizer(infile):
    file, ext = os.path.splitext(infile)
    with Image.open(infile) as im:
        new_image = im.resize((basewidth, size), Image.ANTIALIAS)
        new_image.mode = 'RGB'
        new_image.save(file + "_resized.jpg", "JPEG")

if __name__ == "__main__":
    resizer('uploads/photo.jpg')
