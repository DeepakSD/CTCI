'''
Created on Jun 14, 2017

@author: deepaks
'''
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
class Line:
    epsilon=0.001
    infinite_slope=False
    slope=1
    def __init__(self,p,q):
        if (p.x-q.x) > self.epsilon:
            self.slope=(p.y-q.y)/(p.x-q.x)
            self.intercept=p.y-slope*p.x
        else:
            self.infinite_slope=True
            self.intercept=p.x
    
    def floorToNearestEpsilon(self,d):
        temp = int(d/self.epsilon)
        return temp*self.epsilon
    
    def isEquivalent_1(self,a,b):
        return abs(a-b)<self.epsilon
    
    def isEquivalent(self,lineObject):
        if self.isEquivalent_1(lineObject.slope,self.slope) and self.isEquivalent_1(lineObject.intercept, self.intercept) and self.infinite_slope==lineObject.infinite_slope:
            return True
        return False
    
def findBestLine(points):
    linesBySlope = getListofLines(points)
    return getBestLine(linesBySlope)
    
def getListofLines(points):
    linesBySlope = dict()
    for i in range(len(points)):
        for j in range(i+1,len(points)):
            line = Line(points[i],points[j])
            key = line.floorToNearestEpsilon(line.slope)
            if key not in linesBySlope:
                linesBySlope[key]=[line]
            else:
                linesBySlope[key].append(line)
    return linesBySlope

def getBestLine(linesBySlope):
    bestLine=None
    bestCount=0
    slopes=linesBySlope.keys()
    for slope in slopes:
        lines=linesBySlope[slope]
        for line in lines:
            count = countEquivalentLines(linesBySlope,line)
            if count > bestCount:
                bestCount = count
                bestLine = line
    return bestLine

def countEquivalentLines(linesBySlope,line):
    key = line.floorToNearestEpsilon(line.slope)
    count = countEquivalentLines_1(linesBySlope[key], line)
    count+=countEquivalentLines_1(linesBySlope[key-Line.epsilon], line)
    count+=countEquivalentLines_1(linesBySlope[key+Line.epsilon], line)
    return count

def countEquivalentLines_1(lines,line):
    if lines is None:
        return 0
    count=0
    for parallelLine in lines:
        if parallelLine.isEquivalent(line):
            count+=1
    return count


n_points=50
points=[-1]*n_points
for i in range(n_points/2):
    p = Point(i, 2.3 * i + 20.0)
    points[i] = p
    
for i in range(n_points/2-1):
    p = Point(i, 3.0 * i + 1.0)
    points[n_points / 2 + i] = p

print findBestLine(points)
    
