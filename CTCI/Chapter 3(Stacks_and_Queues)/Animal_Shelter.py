'''
Created on May 27, 2017

@author: deepaks
'''
from collections import deque
class Solution:
    def __init__(self):
        self.dogQueue=deque()
        self.catQueue=deque()
        self.timestamp=0
        
    def enqueue(self,animal_type,animal_name):
        if animal_type=="dog":
            self.dogQueue.appendleft((animal_name,self.timestamp))
            self.timestamp+=1
        elif animal_type=="cat":
            self.catQueue.appendleft((animal_name,self.timestamp))
            self.timestamp+=1
        else:
            print "Invalid animal type"
            
    def dequeueAny(self):
        dog=self.dogQueue.pop() if not len(self.dogQueue)==0 else (None,-1)
        cat=self.catQueue.pop() if not len(self.catQueue)==0 else (None,-1)
        if dog[1]==-1 and cat[1]==-1:
            return None
        elif dog[1]<cat[1]:
            self.catQueue.append(cat)
            return dog[0]
        else:
            self.dogQueue.append(dog)
            return cat[0]
    
    def dequeueCat(self):
        if not len(self.catQueue)==0:
            return self.catQueue.pop()[0]
        
    def dequeueDog(self):
        if not len(self.dogQueue)==0:
            return self.dogQueue.pop()[0]
        

sol=Solution()
sol.enqueue("cat", "cat1")
sol.enqueue("cat", "cat2")
sol.enqueue("dog", "dog1")
print sol.dequeueAny()
print sol.dequeueDog()
        
        
        