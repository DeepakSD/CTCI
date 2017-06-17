'''
Created on May 27, 2017

@author: deepaks
'''
class Stack:
    def __init__(self):
        self.stack=[]
        self.size=0
        
    def push(self,item):
        self.stack.append(item)
        self.size+=1
        
    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is Empty")
        self.size-=1
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack)==0
            
    
    def sort(s):
        r=Stack()
        while not s.isEmpty():
            temp=s.pop()
            while not r.isEmpty() and r.peek()>temp:
                s.push(r.pop())
            r.push(temp)
        
        while not r.isEmpty():
            s.push(r.pop())
        return s
        
stack=Stack()
stack.push(9)
stack.push(2)
stack.push(7)
stack.push(1)
stack.push(5)
sstack=Stack.sort(stack)
print sstack.pop()
print sstack.pop()
print sstack.pop()
print sstack.peek()


