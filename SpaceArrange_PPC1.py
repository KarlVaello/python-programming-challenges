from random import randint
import math

# def that sort an array of points (bubble algorithm)
def bubbleSort(alist):
    n = len(alist)
    for i in range(len(alist)-1):
        swp = False
        for j in range(len(alist)-1):
            if (alist[j][4] > alist[j+1][4]):
                tempPoint =  alist[j]
                alist[j] = alist[j+1]
                alist[j+1] = tempPoint
                swp = True

        if (swp == False):
            break

nPoint = 9 # numer of points
points = [] # points array

pointRange = 90 #aleatory range

# loop to create new random points
for x in range (nPoint):
    newPoint=[x+1,randint(-pointRange,pointRange),randint(-pointRange,pointRange),randint(-pointRange,pointRange)]  
    points.append(newPoint)

# loop to print element on creation order
print("Element on creation order [x,y,z]")
for i in range(nPoint):
    print(points[i])
    
print()
# loop to calculate distance to [0, 0, 0] of each point
print("Element on creation order [x,y,z, DistanceTo0,0,0]")
for e in range (nPoint):
    d = math.sqrt(((points[e][1]-0)**2)+((points[e][2]-0)**2)+((points[e][3]-0)**2))
    points[e].append(d)
    
# loop to print element on creation order and distance to [0, 0, 0]
for i in range(nPoint):
    print(points[i])
    
# bubble sort algorithm
bubbleSort(points)

print()
# print elements in order
print("Elements ordered by distance")
for i in range(nPoint):
    print(points[i])
    


    
    
