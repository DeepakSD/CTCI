'''
Created on Jun 6, 2017

@author: deepaks
'''
def paintFill(screen,x,y,nColor):
    if screen[x][y]==nColor:
        return False
    paint(screen,x,y,screen[x][y],nColor)
    return screen

def paint(screen,x,y,oColor,nColor):
    if x<0 or x>=len(screen) or y<0 or y>=len(screen[0]):
        return
    
    if screen[x][y]==oColor:
        screen[x][y]=nColor
        paint(screen,x-1,y,oColor,nColor)
        paint(screen,x+1,y,oColor,nColor)
        paint(screen,x,y-1,oColor,nColor)
        paint(screen,x,y+1,oColor,nColor)
        

screen = [[1,1,1,1,1],
          [1,2,2,2,1],
          [1,2,3,2,1],
          [1,2,2,2,1],
          [1,1,1,1,1]]
print paintFill(screen,0,0,1)