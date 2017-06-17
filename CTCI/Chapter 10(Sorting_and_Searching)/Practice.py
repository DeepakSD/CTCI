'''
Created on Jun 9, 2017

@author: deepaks
'''
def searchMatrix1(matrix,target): # Time Complexity: O(log(M+N))
    return findElement(matrix,target,[0,0],[len(matrix)-1,len(matrix[0])-1])

def findElement(matrix,target,origin,dest):
    if not inbounds(matrix, origin) or not inbounds(matrix, dest):
        return None
    if matrix[origin[0]][origin[1]]==target:
        return tuple(origin)
    elif not isBefore(origin, dest):
        return None
    
    start=origin[:]
    diagonalDistance=min(dest[0]-origin[0],dest[1]-origin[1])
    end=[start[0]+diagonalDistance,start[1]+diagonalDistance]
    p=[0,0]
    while isBefore(start,end):
        p=setToAverage(start, end)
        if target > matrix[p[0]][p[1]]:
            start[0]=p[0]+1
            start[1]=p[1]+1
        else:
            end[0]=p[0]-1
            end[1]=p[1]-1
    return partitionAndSearch(matrix, origin, dest, start, target)

def partitionAndSearch(matrix,origin,dest,pivot,target):
    lowerLeftorigin=[pivot[0],origin[1]]
    lowerLeftDest=[dest[0],pivot[1]-1]
    upperRightorigin=[origin[1],pivot[0]]
    upperRightDest=[pivot[0]-1,dest[1]]
    result=findElement(matrix, target, lowerLeftorigin, lowerLeftDest)
    if result is None:
        return findElement(matrix, target, upperRightorigin, upperRightDest)
    return result
    
def inbounds(matrix,coordinate):
    r,c=coordinate
    return r>=0 and c>=0 and r<len(matrix) and c<len(matrix[0])

def isBefore(origin,dest):
    return origin[0]<=dest[0] and origin[1]<=dest[1]

def setToAverage(origin,dest):
    return [(origin[0]+dest[0])//2,(origin[1]+dest[1])//2]

matrix=[[ 15 , 20 , 40 , 85  ],
        [ 20 , 35 , 80 , 95  ],
        [ 30 , 55 , 95 , 105 ],
        [ 40 , 80 , 100, 120 ]]
target=55
print searchMatrix1(matrix, target)