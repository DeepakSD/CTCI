'''
Created on Apr 18, 2017

@author: deepaks
'''
def nullify(matrix):
    rowHasZero=False
    colHasZero=False
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==0:
                if i==0: rowHasZero=True
                if j==0: colHasZero=True
                matrix[i][0]=0
                matrix[0][j]=0
                
    for i in range(1,len(matrix)):
        for j in range(1,len(matrix[0])):
            if matrix[i][0]==0 or matrix[0][j]==0:
                matrix[i][j]=0
            
    if rowHasZero:
        for i in range(len(matrix[0])):
            matrix[0][i]=0
    
    if colHasZero:
        for i in range(len(matrix)):
            matrix[i][0]=0
    
    return matrix
    
       
matrix=[[1, 2, 3, 4, 0],
        [6, 0, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 0, 18, 19, 20],
        [21, 22, 23, 24, 25]]
print nullify(matrix)