'''
Created on Jun 4, 2017

@author: deepaks
'''
def getPath(maze):
    if maze is None or len(maze)==0:
        return False
    cache=dict()
    path=list()
    if _getPath(maze,len(maze)-1,len(maze[0])-1,cache,path):
        return path
    return None

def _getPath(maze,r,c,cache,path): 
    if r<0 or c<0 or not maze[r][c]:
        return False
    
    try:
        return cache[(r,c)]
    except KeyError:
        success=False
        if (r==0 and c==0) or _getPath(maze,r,c-1,cache,path) or _getPath(maze,r-1,c,cache,path):
            path.append((r,c))
            success=True
        
        cache[(r,c)]=success
        return success
        

maze=[[1,1,0,0,1],
      [0,1,1,1,0],
      [0,0,0,1,1],
      [1,0,1,0,1]]
print getPath(maze)