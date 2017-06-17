'''
Created on Jun 4, 2017

@author: deepaks
'''
def nQueens(n):
    ways=[]
    placeQueens(n,0,[],ways)
    return ways

def placeQueens(n,c,queens,ways):
    if c==n:
        ways.append(queens)
        
    for r in range(n):
        position=[r,c]
        if checkValid(queens,position):
            queensTemp=queens[:]
            queensTemp.append(position)
            placeQueens(n,c+1,queensTemp,ways)

def checkValid(queens,position):
    for queen in queens:
        if queen[0]==position[0]:
            return False
        
        if queen[1]==position[1]:
            return False
        
        if (abs(queen[0]-position[0]) == abs(queen[1]-position[1])):
            return False
    return True
        
print len(nQueens(4))