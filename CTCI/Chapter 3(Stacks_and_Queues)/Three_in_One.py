'''
Created on May 27, 2017

@author: deepaks
'''
class Multistack:
    def __init__(self,stacksize):
        self.numstacks=3
        self.array=[0]*(stacksize*self.numstacks)
        self.sizes=[0]*self.numstacks
        self.stacksize=stacksize
    
    def push(self,item,stacknum):
        if self.isFull(stacknum):
            raise Exception("Stack is Full")
        self.sizes[stacknum]+=1
        self.array[self.indexOfTop(stacknum)]=item
    
    def pop(self,stacknum):
        if self.isEmpty(stacknum):
            raise Exception("Stack is Empty")
        value=self.array[self.indexOfTop(stacknum)]
        self.array[self.indexOfTop(stacknum)]=0
        self.sizes[stacknum]-=1
        return value
    
    def peek(self,stacknum):
        if self.isEmpty(stacknum):
            raise Exception("Stack is empty")
        return self.array[self.indexOfTop(stacknum)]
    
    def isEmpty(self, stacknum):
        return self.sizes[stacknum]==0
    
    def isFull(self,stacknum):
        return self.sizes[stacknum]==self.stacksize
    
    def indexOfTop(self,stacknum):
        offset=self.stacksize*stacknum
        return offset+self.sizes[stacknum]-1
    
    
newstack=Multistack(2)
print newstack.isEmpty(1)
newstack.push(3, 1)
print newstack.peek(1)
print newstack.isEmpty(1)
newstack.push(2, 0)
print newstack.peek(0)
print newstack.pop(1)
#print newstack.peek(1)
newstack.push(3, 1)
