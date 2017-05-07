from colorMath import *
from fileOutput import outputDictToFile
from imageReading import readPixelsToDic
from collections import defaultdict
import csv

def comparePixelToColors(imagePixels):

    pxColorNamed = defaultdict(int)
    listOfColors = defaultdict(int)

    with open('ColorList.csv') as infile:
        reader = csv.DictReader(infile, delimiter=';')
        for row in reader:
            listColorRGB = (int(row['R']), int(row['G']), int(row['B']))
            listOfColors[(listColorRGB)] = row['Name']

    for color in imagePixels:

        if color in listOfColors:
            pxColorNamed[listOfColors[color]] += imagePixels[color]
        else:

            colorLAB1 = convRGBtoLAB(color)
            bestMatch = [500, " "]

            for listColor in listOfColors:

                colorLAB2 = convRGBtoLAB(listColor)

                dif = deltaE_1994(colorLAB1, colorLAB2)

                if dif < bestMatch[0]:
                    bestMatch[0] = dif
                    bestMatch[1] = listOfColors[listColor]

            pxColorNamed[bestMatch[1]] += imagePixels[color]

    outputDictToFile('imagePixels.csv', imagePixels)
    outputDictToFile('pxColorNamed.csv', pxColorNamed)
    outputDictToFile('listOfColors.csv', listOfColors)
