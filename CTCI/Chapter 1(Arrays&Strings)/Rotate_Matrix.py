'''
Created on Apr 6, 2017

@author: deepaks
'''
def rotateMatrix(matrix):##Clockwise 90 degree rotation
    if len(matrix)==0 or len(matrix)!=len(matrix[0]):
        return False
    n=len(matrix)
    for layer in range(n//2):
        first=layer
        last=n-1-layer
        for i in range(first,last):
            offset=i-first
            top=matrix[first][i] ##Save Top
        #Left->Top
            matrix[first][i]=matrix[last-offset][first]
        #Bottom->Left
            matrix[last-offset][first]=matrix[last][last-offset]
        #Right->Bottom
            matrix[last][last-offset]=matrix[i][last]
        #Top->right
            matrix[i][last]=top
    return matrix 


def rotateMatrix(matrix):##AntiClockwise 90 degree rotation
    if len(matrix)==0 or len(matrix)!=len(matrix[0]):
        return False
    
    n=len(matrix)
    for layer in range(n//2):
        first=layer
        last=n-1-layer
        for i in range(first,last):
            offset=i-first
            top=matrix[first][i]
            
            matrix[first][i]=matrix[i][last]
            matrix[i][last]=matrix[last][last-offset]
            matrix[last][last-offset]=matrix[last-offset][first]
            
            matrix[last-offset][first]=top
    
    return matrix    
        
    


matrix=[[1,2,3,4,5],
        [6,7,8,9,10],
        [11,12,13,14,15],
        [16,17,18,19,20],
        [21,22,23,24,25]]
print rotateMatrix(matrix)