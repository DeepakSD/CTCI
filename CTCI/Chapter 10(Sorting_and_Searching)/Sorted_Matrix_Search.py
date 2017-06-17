'''
Created on Jun 9, 2017

@author: deepaks
'''
def searchMatrix(matrix,target): #Time complexity: O(M+N)
    m,n=len(matrix),len(matrix[0])
    r=0
    c=n-1
    while r<m and c>=0:
        if matrix[r][c]==target:
            return True
        elif matrix[r][c]>target:
            c-=1
        else:
            r+=1
    return False

def searchMatrix1(matrix,target): # Time Complexity: O(log(M+N))
    return findElement(matrix,target,[0,0],[len(matrix)-1,len(matrix[0])-1])

def findElement(matrix,target,origin,dest):
    if not inbounds(matrix,origin) or not inbounds(matrix,dest):
        return None
    if matrix[origin[0]][origin[1]]==target:
        return tuple(origin)
    elif not isBefore(origin,dest):
        return None
    start=origin[:]
    diagonalDistance=min(dest[1]-origin[1],dest[0]-origin[0])
    end=[start[0]+diagonalDistance,start[1]+diagonalDistance]
    p=[0,0]
    while isBefore(start,end):
        p=setToAverage(start,end)
        if target > matrix[p[0]][p[1]]:
            start[0]=p[0]+1
            start[1]=p[1]+1
        else:
            end[0]=p[0]-1
            end[1]=p[1]-1
    return partitionAndSearch(matrix,origin,dest,start,target)

def partitionAndSearch(matrix,origin,dest,pivot,target):
    lower_left_origin = [pivot[0], origin[1]]
    lower_left_dest = [dest[0], pivot[1]-1]
    upper_right_origin = [origin[0], pivot[1]]
    upper_right_dest = [pivot[0]-1, dest[1]]
    lower_left = findElement(matrix,target, lower_left_origin, lower_left_dest)
    if lower_left is None:
        return findElement(matrix,target, upper_right_origin, upper_right_dest)
    return lower_left

def inbounds(matrix,coordinate):
    r,c=coordinate
    return r>=0 and c>=0 and r<len(matrix) and c<len(matrix[0])

def isBefore(origin,dest):
    return origin[0]<=dest[0] and origin[1]<=dest[1]

def setToAverage(origin,dest):
    return [(origin[0] + dest[0]) // 2, (origin[1] + dest[1]) // 2]


matrix=[[ 15 , 20 , 40 , 85  ],
        [ 20 , 35 , 80 , 95  ],
        [ 30 , 55 , 95 , 105 ],
        [ 40 , 80 , 100, 120 ]]
target=55
print searchMatrix1(matrix, target)