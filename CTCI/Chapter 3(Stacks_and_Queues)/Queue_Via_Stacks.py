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
        if len(self.stack)==0:
            raise Exception("Stack is Empty")
        self.size-=1
        return self.stack.pop()
    
    def peek(self):
        if len(self.stack)==0:
            raise Exception("Stack is empty")
        return self.stack[-1]


class Queue:
    def __init__(self):
        self.stackOldest=Stack()
        self.stackNewest=Stack()
        
    def enqueue(self,item):
        self.stackNewest.push(item)
        
    def dequeue(self):
        if self.stackOldest.size==0:
            self.rebuild()
        return self.stackOldest.pop()
    
    def peekFront(self):
        if self.stackOldest.size==0:
            self.rebuild()
        return self.stackOldest.peek()
    
    def rebuild(self):
        while self.stackNewest.size>0:
            self.stackOldest.push(self.stackNewest.pop())
    

queue=Queue()
queue.enqueue(7)
queue.enqueue(9)
print queue.peekFront()

