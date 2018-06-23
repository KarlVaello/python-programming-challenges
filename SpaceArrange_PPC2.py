from random import randint
import math
from Point import Point

# def that sort an array of points (bubble algorithm)
def bubbleSort(alist):
    n = len(alist)
    for i in range(len(alist)-1):
        swp = False
        for j in range(len(alist)-1):
            if (alist[j][2] > alist[j+1][2]):
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
    newPointObjet = Point(randint(-pointRange,pointRange),randint(-pointRange,pointRange),randint(-pointRange,pointRange))
    newPoint = [x+1, newPointObjet]
    points.append(newPoint)


# loop to print element on creation order
print("Element on creation order [x,y,z]")
for i in range(nPoint):
    print("(" + str(points[i][0]) + ",["+ str(points[i][1].getXc())+ ", "+ str(points[i][1].getYc())+ ", "+ str(points[i][1].getZc()) + "])")
    
print()
# loop to calculate distance to [0, 0, 0] of each point
for e in range (nPoint):
    d = math.sqrt(((points[e][1].getXc()-0)**2)+((points[e][1].getYc()-0)**2)+((points[e][1].getYc()-0)**2))
    points[e].append(d)
   
   
# loop to print element on creation order and distance to [0, 0, 0]
print("Element on creation order ( n [x,y,z] / DistanceTo0,0,0]")
for i in range(nPoint):
    print("(" + str(points[i][0]) + ",["+ str(points[i][1].getXc())+ ", "+ str(points[i][1].getYc())+ ", "+ str(points[i][1].getZc()) + "], " + str(points[i][2]) +  ")")
    
# bubble sort algorithm 
bubbleSort(points)

print()
# print elements in order
print("Elements ordered by distance")
for i in range(nPoint):
    print("(" + str(points[i][0]) + ",["+ str(points[i][1].getXc())+ ", "+ str(points[i][1].getYc())+ ", "+ str(points[i][1].getZc()) + "], " + str(points[i][2]) +  ")")
    


    
    
