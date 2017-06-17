'''
Created on Jun 16, 2017

@author: deepaks
'''
def pondSizes(matrix):
    res=[]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==0:
                res.append(computeSize(matrix,i,j))
    return res

def computeSize(matrix,i,j):
    if i<0 or i>=len(matrix) or j<0 or j>=len(matrix[0]) or matrix[i][j]!=0:
        return 0
    
    size=1
    matrix[i][j]=-1
    for r in range(-1,2):
        for c in range(-1,2):
            size+=computeSize(matrix, i+r, j+c)
    return size

matrix=[[0,2,1,0],
        [0,1,0,1],
        [1,1,0,1],
        [0,1,0,1]]
print pondSizes(matrix)