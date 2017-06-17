'''
Created on Jun 10, 2017

@author: deepaks
'''
class Point:  #### Check this question
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def setLocation(self,x,y):
        self.x=x
        self.y=y

class Line:
    def __init__(self,start,end):
        deltaY=end.y-start.y
        deltaX=end.x-start.x
        try:
            self.slope=deltaY/deltaX
        except ZeroDivisionError:
            self.slope=float("inf")
        self.yintercept=end.y-self.slope*end.x


def intersection(start1,end1,start2,end2):
    # Rearranging for simplicity of logic 
    if start1.x > end1.x:
        swap(start1,end1)
    if start2.x > end2.x:
        swap(start2,end2)
    if start1.x > start2.x:
        swap(start1,start2)
        swap(end1,end2)
        
    line1=Line(start1,end1)
    line2=Line(start2,end2)
    
    #If lines are parallel
    if line1.slope==line2.slope:
        if line1.yintercept==line2.yintercept and isBetween(start1,start2,end1):
            return start2
        return None
    
    #Getting intersection point
    x = (line2.yintercept - line1.yintercept)/(line1.slope - line2.slope)
    y = x*line1.slope + line1.yintercept
    intersect = Point(x,y)
    
    if isBetween(start1, intersect, end1) and isBetween(start2, intersect, end2):
        return intersect
    
    return None
      
def swap(point1,point2):
    x=point1.x
    y=point1.y
    point1.setLocation(point2.x,point2.y)
    point2.setLocation(x,y)

def isBetween(start,middle,end):
    return isBetween1(start.x,middle.x,end.x) and isBetween1(start.y, middle.y, end.y) 

def isBetween1(start,middle,end):
    if start > end:
        return end<=middle<=start
    else:
        return start<=middle<=end
    
coordinates=[[2,5],[10,5],[6,8],[6,12]]
result = intersection(Point(coordinates[0][0],coordinates[0][1]), Point(coordinates[1][0],coordinates[1][1]), Point(coordinates[2][0],coordinates[2][1]), Point(coordinates[3][0],coordinates[3][1]))
if result:
    print result.x,result.y
else:
    print result

    
