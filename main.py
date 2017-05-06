from PIL import Image
from collections import defaultdict
from colorMath import *
from fileOutput import *
import csv

myImg = Image.open('1491676804085.png')

imgWidth, imgHeight = myImg.size

pxColor = defaultdict(int)
pxColorNamed = defaultdict(int)
listOfColors = defaultdict(int)

for pixel in list(myImg.getdata()):
    pxColor[pixel] += 1

with open('ColorList.csv') as infile:
    reader = csv.DictReader(infile, delimiter=';')
    for row in reader:
        listColorRGB = (int(row['R']), int(row['G']), int(row['B']))
        listOfColors[(listColorRGB)] = row['Name']

for color in pxColor:

    if color in listOfColors:
        pxColorNamed[listOfColors[color]] += pxColor[color]
    else:

        colorLAB1 = convRGBtoLAB(color)
        bestMatch = [500, " "]

        for listColor in listOfColors:

            colorLAB2 = convRGBtoLAB(listColor)

            dif = deltaE_1994(colorLAB1, colorLAB2)

            if dif < bestMatch[0]:
                bestMatch[0] = dif
                bestMatch[1] = listColor

        pxColorNamed[bestMatch[1]] += pxColor[color]

outputDictToFile('pxColor.csv', pxColor)
outputDictToFile('pxColorNamed.csv', pxColorNamed)
outputDictToFile('listOfColors.csv', listOfColors)
