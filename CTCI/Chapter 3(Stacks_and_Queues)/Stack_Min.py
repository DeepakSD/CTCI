'''
Created on May 27, 2017

@author: deepaks
'''
class Stack:
    def __init__(self,size):
        self.stack=[]
        self.size=size
        self.min=float('inf')
        
    def push(self,item):
        if len(self.stack)==self.size:
            raise Exception("Stack is Full")
        self.min = min(self.min,item)
        self.stack.append((item,self.min))
        
    def pop(self):
        if len(self.stack)==0:
            raise Exception("Stack is Empty")
        return self.stack.pop()[0]
    
    def getMin(self):
        if len(self.stack)==0:
            raise Exception("Stack is Empty")
        return self.stack[-1][1]
    
class Stack1:
    def __init__(self):
        self.stack = []
        self.min = []
        
    def push(self, value):
        self.stack.append(value)
        if len(self.min) == 0 or value <= self.min[-1]:
            self.min.append(value)

    def pop(self):
        if len(self.stack) == 0:
            return None
        data = self.stack.pop()
        if data == self.min[-1]:
            self.min.pop()
        return data

    def get_min(self):
        if len(self.min)==0:
            return None
        return self.min[-1] 
    
    
stack=Stack(6)
stack.push(2)
stack.push(1)
stack.push(6)
stack.push(0)
print stack.getMin()
print stack.pop()
print stack.getMin()

