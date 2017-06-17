'''
Created on May 27, 2017

@author: deepaks
'''
class SetofStacks:
    def __init__(self,size):
        self.stacks=[]
        self.size=size

        
    def push(self,item):
        if len(self.stacks)==0 or len(self.stacks[-1])==self.size :
            self.stacks.append([])
        self.stacks[-1].append(item)
        
    def pop(self):
        if len(self.stacks)==0:
            raise Exception("Stack is Empty")
        value= self.stacks[-1].pop()
        if len(self.stacks[-1])==0:
            self.stacks.pop()
        return value
    
    def popAt(self,index):
        if index<1 or index>len(self.stacks) or len(self.stacks[index-1])==0:
            return None
        return self.stacks[index-1].pop()
     
    
stack=SetofStacks(6)
stack.push(2)
stack.push(1)
stack.push(6)
stack.push(0)