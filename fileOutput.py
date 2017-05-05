import os
import csv

def outputDictToFile(fileName, data):
    filePath = os.path.join(os.getcwd(), "outputFiles", fileName)

    write = csv.writer(open(filePath, 'w'))

    for key, val in data.items():
        write.writerow([key, val])
