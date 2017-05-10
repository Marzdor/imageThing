from imageReading import readPixelsToDic
from pixelProcessing import *
from fileProcessing import moveImage
import os

picToSortPath = os.path.join(os.getcwd(), "imagesToSort")
listOfPics = os.listdir(picToSortPath)

for pic in listOfPics:
    print(pic)
    picPath = os.path.join(picToSortPath, pic)

    listOfColors = comparePixelToColors(readPixelsToDic(picPath))

    mainColor = determineDominateColor(listOfColors)

    moveImage(picPath, mainColor[0])
