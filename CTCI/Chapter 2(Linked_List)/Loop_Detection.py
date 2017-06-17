'''
Created on May 27, 2017

@author: deepaks
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class LinkedList: 
    def __init__(self):
        self.head=None
           
    def insert(self,node):
        if self.head is None:
            self.head=node
            return
        
        temp=self.head
        while temp.next:
            temp=temp.next
        
        temp.next=node
    
    def makeLoop(self):
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=self.head
        
    
    def print_ll(self):
        temp=self.head
        while temp:
            print temp.data,
            temp=temp.next
        print ""
        
class Solution:
    def loopDetection(self,head): # Refer http://www.geeksforgeeks.org/write-a-c-function-to-detect-loop-in-a-linked-list/
        fast = slow =head
        
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if slow == fast:
                break
        
        if fast is None or fast.next is None:
            return None
        
        slow = head ##This block is to get the beginning element of the loop
        while fast!=slow:
            fast=fast.next
            slow =slow.next
            
        return fast.data
        
        
        
ll=LinkedList()
ll.head=Node(5)
ll.insert(Node(1))
ll.insert(Node(2))
ll.insert(Node(3))
ll.insert(Node(6))
ll.insert(Node(1))
ll.insert(Node(2))
ll.insert(Node(8))
ll.makeLoop()
#ll.print_ll()

sol=Solution()
print sol.loopDetection(ll.head)