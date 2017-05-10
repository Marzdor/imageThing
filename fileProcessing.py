import os
import shutil
import csv

def outputDictToFile(fileName, data):
    filePath = os.path.join(os.getcwd(), "outputFiles", fileName)

    write = csv.writer(open(filePath, 'w'))

    for key, val in data.items():
        write.writerow([key, val])


def moveImage(filePath, dominateColor):
    picSortedPath = os.path.join(os.getcwd(), "imagesSorted")

    picPath = os.path.join(picSortedPath, dominateColor, os.path.basename(filePath))

    shutil.move(filePath, picPath)
