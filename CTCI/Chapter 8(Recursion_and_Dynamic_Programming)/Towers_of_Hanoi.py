'''
Created on Jun 5, 2017

@author: deepaks
'''
class Tower:
    def __init__(self,n):
        self.disks=list()
    
    def add(self,d):
        if len(self.disks)!=0 and self.disks[-1] <=d:
            print "Error placing disk"+str(d)
        else:
            self.disks.append(d)
    
    def moveTopTo(self,t):
        top=self.disks.pop()
        t.add(top)
    
    def moveDisks(self,n,destination,buffer):
        if n>0:
            self.moveDisks(n-1,buffer,destination)
            self.moveTopTo(destination)
            buffer.moveDisks(n-1,destination,self)
    
    
n=3
towers=[]
for i in range(n):
    towers.append(Tower(i))

for i in range(n-1,-1,-1):
    towers[0].add(i)

towers[0].moveDisks(n,towers[2],towers[1])
print towers[2].disks.pop()
print towers[2].disks.pop()
print towers[2].disks.pop()
