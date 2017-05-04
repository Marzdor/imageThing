from PIL import Image
from collections import defaultdict
from colorMath import *
import csv

myImg = Image.open('testImg.jpg')

imgWidth, imgHeight = myImg.size

pxColor = defaultdict(int)
pxColorNamed = defaultdict(int)

for pixel in list(myImg.getdata()):
    pxColor[pixel] += 1

with open('ColorList.csv', mode="r") as infile:
    reader = csv.reader(infile)
    with open('ColorList.csv', mode='w') as outfile:
        listOfColors = {rows[0]:rows[1] for rows in reader}

for color in pxColor:

    colorLAB1 = convRGBtoLAB(color)
    bestMatch = [500, " "]

    for listColor in listOfColors:

        colorLAB2 = convRGBtoLAB(listOfColors[listColor])

        dif = deltaE_1994(colorLAB1, colorLAB2)

        print("diff = ", dif, "bestMatch[0] = ", bestMatch[0])

        if dif < bestMatch[0]:
            bestMatch[0] = dif
            bestMatch[1] = listColor

    pxColorNamed[bestMatch[1]] = pxColor[color]

for px in pxColorNamed:

    print("Key : " , px, " ", "Value : ", pxColorNamed[px])
