'''
Created on May 26, 2017

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
    
    def print_ll(self):
        temp=self.head
        while temp:
            print temp.data,
            temp=temp.next
        print ""
class Solution:
    def deleteMiddle(self,node):## Access to only that node
        node.data=node.next.data
        node.next=node.next.next
        return
        
        
        
ll=LinkedList()
ll.head=Node(0)
ll.insert(Node(1))
ll.insert(Node(2))
ll.insert(Node(3))
middlenode=ll.insert(Node(6))
ll.insert(Node(1))
ll.insert(Node(2))
ll.insert(Node(8))
ll.print_ll()
sol=Solution()
ll.head=sol.deleteMiddle(middlenode)
ll.print_ll()