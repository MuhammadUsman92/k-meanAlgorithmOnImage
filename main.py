# Import the necessary libraries
import numpy
from PIL import Image
from numpy import asarray
import random
import math

# load the image and convert into
# numpy array
img = Image.open('pic1.jpg')
numpydata = asarray(img)


lis = numpydata.tolist()
count = 0
for i in lis:
    count += 1
    # print(len(i))

row, col, element = numpydata.shape
print('row', row)
# 3

print('col', col)
# 4
print(f"numpydata.shape {numpydata.shape}")
randomList = {'A': [41, 36, 42], 'B': [45, 88, 104]}
def calculateDistance(lis):
    distance = math.sqrt((lis[0]-randomList['A'][0])**2 + (lis[1]-randomList['A'][1])**2 + (lis[2]-randomList['A'][2])**2)
    centroid = 'A'
    c = centroid
    for i in randomList:
        if math.sqrt((lis[0]-randomList[i][0])**2 + (lis[1]-randomList[i][1])**2 + (lis[2]-randomList[i][2])**2) < distance:
            distance = math.sqrt((lis[0]-randomList[i][0])**2 + (lis[1]-randomList[i][1])**2 + (lis[2]-randomList[i][2])**2)
            c=centroid
        centroid = chr(ord(centroid) + 1)
    # print(distance)
    # print(c)
    return c

def find_nearest(array, value):
    array = numpy.asarray(array)
    idx = (numpy.abs(array - value)).argmin()
    print(idx)
    return array[idx]


if __name__ == '__main__':
    c='A'
    # for k in range(0, 2):
    #     randomRow = random.randint(0, row)
    #     randomCol = random.randint(0, col)
    #     randomList[c] = ((numpydata[randomRow, randomCol]).tolist())
    #     c = chr(ord(c) + 1)
        # print(randomRow)
        # print(randomCol)
    print(randomList)
    for i in range(0,15):
        groups={'A':[],'B':[]}
        for i in range(0,row):
            for j in range(0,col):
                groups[calculateDistance(numpydata[i,j])].append(numpydata[i,j].tolist())
        arrayA = numpy.array(groups['A'])
        arrayB = numpy.array(groups['B'])
        randomList['A'] = ((find_nearest(arrayA, numpy.mean(arrayA, axis = 0))).tolist())
        randomList['B'] = ((find_nearest(arrayB, numpy.mean(arrayB, axis=0))).tolist())
        # calculateDistance([189, 178, 132])