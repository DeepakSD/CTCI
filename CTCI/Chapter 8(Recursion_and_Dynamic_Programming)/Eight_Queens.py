'''
Created on Jun 7, 2017

@author: deepaks
'''
def nQueens(n):
    ways = []
    placeQueens(n, 0, [], ways)
    return ways

def placeQueens(n, c, queens, ways):
    if c == n:
        ways.append(queens)
        return None
    for r in range(n):
        position = [ r, c ]
        if checkValid(position, queens):
            queens_cp = queens[:]
            queens_cp.append(position)
            placeQueens(n, c+1, queens_cp, ways)

def checkValid(position, queens):
    for queen in queens:
        if queen[0] == position[0]:
            return False
        if queen[1] == position[1]:
            return False
    # For checking diagonals: if distance between columns equals the distance between the rows then they are in same diagonal
        if (abs(queen[0] - position[0]) == abs(queen[1] - position[1])): 
            return False
    return True

print len(nQueens(4))