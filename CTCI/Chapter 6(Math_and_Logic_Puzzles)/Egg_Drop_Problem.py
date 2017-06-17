'''
Created on Jun 1, 2017

@author: deepaks
'''
class Solution:
    breakingPoint=49
    countDrops=0
    
    def drop(self,floor):
        self.countDrops+=1
        return floor>=self.breakingPoint
    
    def findBreakingPoint(self,floors):
        previousFloor=0
        interval=14
        egg1=interval
        
        while not self.drop(egg1) and egg1<=floors:
            interval-=1
            previousFloor=egg1
            egg1+=interval
        
        egg2=previousFloor+1
        while egg2<=floors and egg2<egg1 and not self.drop(egg2):
            egg2+=1
            
        print self.countDrops
        return egg2 if egg2<floors else -1

sol=Solution()
print sol.findBreakingPoint(100)