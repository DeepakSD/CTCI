'''
Created on Jun 10, 2017

@author: deepaks
'''
class Check:
    def __init__(self,row,column,rowI,colI):
        self.row=row
        self.column=column
        self.rowIncrement=rowI
        self.columnIncrement=colI
    
    def increment(self):
        self.row+=self.rowIncrement
        self.column+=self.columnIncrement
        
    def inBounds(self,size):
        return self.row>=0 and self.row<size and self.column>=0 and self.column<size

def hasWon(board):
    if len(board)==0 or len(board)!=len(board[0]):
        return -1
    
    size=len(board)
    
    instructions=[]
    for i in range(len(board)):
        instructions.append(Check(i,0,0,1))
        instructions.append(Check(0,i,1,0))
    instructions.append(Check(0,0,1,1))  ## For diagonals
    instructions.append(Check(0,size-1,1,-1))
    
    for instr in instructions:
        winner=hasWon1(board,instr)
        if winner!=0:
            return winner
    return -1

def hasWon1(board,instr):
    first=board[instr.row][instr.column]
    while instr.inBounds(len(board)):
        if board[instr.row][instr.column]!=first:
            return 0
        instr.increment()
    return first

board=[[0,1,1],
       [2,1,2],
       [1,2,1]]
print hasWon(board)