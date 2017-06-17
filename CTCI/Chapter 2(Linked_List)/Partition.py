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
    def partition(self,head,x): # Without order
        curr=tail=head
        while curr:
            nextNode=curr.next
            curr.next=None
            if curr.data<x:
                curr.next=head
                head=curr
            else:
                tail.next=curr
                tail=curr
            curr=nextNode
        
        if tail.next is not None:
            tail.next=None
        return head
    
    def partition1(self,head,x):
        l1=h1=Node(0)
        l2=h2=Node(0)

        while head:
            if head.data<x:
                l1.next=head
                l1=l1.next
            else:
                l2.next=head
                l2=l2.next
            
        l2.next=None
        l1.next=h2.next
        
        h1=h1.next
        while h1:
            print h1.data,
            h1=h1.next
        
    
ll=LinkedList()
ll.head=Node(0)
ll.insert(Node(1))
ll.insert(Node(2))
ll.insert(Node(3))
ll.insert(Node(6))
ll.insert(Node(1))
ll.insert(Node(2))
ll.insert(Node(8))
ll.print_ll()
sol=Solution()
ll.head=sol.partition1(ll.head,4)
#ll.print_ll()