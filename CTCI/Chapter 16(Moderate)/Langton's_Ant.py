'''
Created on Jun 17, 2017

@author: deepaks
'''
class Board:
    white=set()
    ant=Ant()
    
class Ant:
    position = Position(0,0)
    orientation = Orientation.right
    
    def turn(self,clockwise):
        self.orientation = self.orientation.getTurn(clockwise)
    
    def move(self):
        if self.orientation==Orientation.left:
            self.position.column-=1
        elif self.orientation==Orientattion.right:
            self.position.column+=1
        elif self.orientation==Orientattion.up:
            self.position.row-=1
        elif self.orientation==orientation.down:
            self.position.row+=1
    
    def adjustPosition(self,shiftRow,shiftColumn):
        self.position.row+=shiftRow
        self.position.column+=shiftColumn
        
class Position:
    def __init__(self,row,column):
        self.row=row
        self.column=column
    
    
        