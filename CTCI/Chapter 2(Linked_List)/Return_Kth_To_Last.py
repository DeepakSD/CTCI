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
    def kthToLast(self,head,k):# Recursive O(n) space
        self.index=0
        return self.helper(head,k)
        
    def helper(self,head,k):
        if head is None:
            return None
        
        node=self.helper(head.next,k)
        self.index+=1
        
        if self.index==k:
            return head.data
        
        return node
    
    def kthToLast1(self,head,k): # O(n) time but O(1) space
        curr=runner=head
        
        for _ in range(k):
            if runner is None:
                return None
            runner=runner.next
            
        while runner:
            curr=curr.next
            runner=runner.next
            
        return curr.data
            
        
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
print sol.kthToLast1(ll.head,2)