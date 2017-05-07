from PIL import Image
from collections import defaultdict

def readPixelsToDic(imageName):
    theImage = Image.open(imageName)

    pxColor = defaultdict(int)

    for pixel in list(theImage.getdata()):
        pxColor[pixel] += 1

    return pxColor
