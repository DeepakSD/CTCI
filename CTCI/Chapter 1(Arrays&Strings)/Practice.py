'''
Created on May 25, 2017

@author: deepaks
'''
def nullify(matrix):
    rowhasZero=False
    colhasZero=False
    
    for i in range(len(matrix)):
        if matrix[i][0]==0:
            colhasZero=True
            break
    for i in range(len(matrix[0])):
        if matrix[0][i]==0:
            rowhasZero=True
            break
    
    for i in range(1,len(matrix)):
        for j in range(1,len(matrix[0])):
            if matrix[i][j]==0:
                matrix[i][0]=0
                matrix[0][j]=0
    
    for i in range(1,len(matrix)):
        if matrix[i][0]==0:
            nullifyRow(matrix,i)
    
    for i in range(1,len(matrix[0])):
        if matrix[0][i]==0:
            nullifyCol(matrix,i)
            
    if rowhasZero:
        nullifyRow(matrix,0)
    if colhasZero:
        nullifyCol(matrix,0)
        
    return matrix
            
            
def nullifyRow(matrix,row):
    for i in range(len(matrix[0])):
        matrix[row][i]=0
        
def nullifyCol(matrix,col):
    for i in range(len(matrix)):
        matrix[i][col]=0
        
   

matrix=[[1, 2, 3, 4, 0],
        [6, 0, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 0, 18, 19, 20],
        [21, 22, 23, 24, 25]]
print nullify(matrix)