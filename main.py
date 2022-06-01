# Import the necessary libraries
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

def calculateDistance(lis):
    distance = math.sqrt((lis[0]-randomList[0][0])**2 + (lis[1]-randomList[0][1])**2 + (lis[2]-randomList[0][2])**2)
    centroid = 'A'
    for i in randomList:
        if math.sqrt((lis[0]-i[0])**2 + (lis[1]-i[1])**2 + (lis[2]-i[2])**2) < distance:
            distance
    print(distance)


randomList = []
for k in range(0, 2):
    randomRow = random.randint(0, row)
    randomCol = random.randint(0, col)
    randomList.append((numpydata[randomRow, randomCol]).tolist())
    # print(randomRow)
    # print(randomCol)
print(randomList)
calculateDistance([189, 178, 132])