'''
Created on May 28, 2017

@author: deepaks
'''
class graph:
    def __init__(self,data):
        self.data=data
        self.neighbors=[]
        
from collections import deque
class Solution:
    def isRoute(self,start,end):
        if start==end:
            return True
        queue=deque([start])
        visited=set([start])
        while len(queue)!=0:
            node=queue.popleft()
            for n in node.neighbors:
                if n not in visited:
                    if n==end:
                        return True
                    visited.add(n)
                    queue.append(n)
        return False
                    
   
n1=graph(1)
n2=graph(2)
n3=graph(3)
n4=graph(4)
n5=graph(5)
n6=graph(6)
n1.neighbors.append(n2)
n2.neighbors.append(n3)
n2.neighbors.append(n4)
n4.neighbors.append(n1)
n4.neighbors.append(n5)

source=n5
destination=n1
sol=Solution()
print sol.isRoute(source, destination)