'''
Created on Jun 13, 2017

@author: deepaks
'''
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Line:
    def __init__(self,start,end):
        self.start=start
        self.end=end

class Square:
    def __init__(self,left,top,size):
        self.left=left
        self.top=top
        self.bottom=top+size
        self.right=left+size
        self.size=size
    
    def middle(self):
        return Point((self.left+self.right)/2.0,(self.bottom+self.top)/2.0)
    
    def extend(self,mid1,mid2,size):
        xdir = -1 if mid1.x<mid2.x else 1
        ydir = -1 if mid1.y<mid2.y else 1
        
        if mid1.x==mid2.x: # Slope will give infinity so doing this step
            return Point(mid1.x,mid1.y+ydir*size/2.0)
        slope=(mid1.y - mid2.y) / (mid1.x - mid2.x)
        x1=0
        y1=0
        
        if abs(slope)==1:
            x1=mid1.x + xdir * size / 2.0
            y1=mid1.y + ydir * size / 2.0
        elif abs(slope)<1:
            x1 = mid1.x + xdir * size / 2.0
            y1 = slope * (x1 - mid1.x) + mid1.y
        else:
            y1 = mid1.y + ydir * size / 2.0
            x1 = (y1 - mid1.y) / slope + mid1.x
        return Point(x1,y1)
        
    def cut(self,sq2):
        p1=self.extend(self.middle(),sq2.middle(),self.size)
        p2=self.extend(self.middle(),sq2.middle(),-1 * self.size)
        p3=self.extend(sq2.middle(),self.middle(),sq2.size)
        p4=self.extend(sq2.middle(),self.middle(),-1 * sq2.size)
            
        start=p1
        end=p1
        points=[p2,p3,p4]
        for point in points:
            if (point.x < start.x) or (point.x==start.x and point.y<start.y):
                start=point
            elif (point.x > end.x) or (point.x==end.x and point.y>end.y):
                end=point
            
        return Line(start,end)

sq1=Square(10,10,10)
sq2=Square(4,4,3)       
result = sq1.cut(sq2)
print result.start.x,result.start.y
print result.end.x,result.end.y   
    
