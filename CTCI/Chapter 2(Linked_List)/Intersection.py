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
    
    def print_ll(self):
        temp=self.head
        while temp:
            print temp.data,
            temp=temp.next
        print ""

class Solution:
    def intersection(self,head1,head2):
        tail1,len1=self.tailAndSize(head1)
        tail2,len2=self.tailAndSize(head2)
        
        if tail1!=tail2:
            print "No intersection"
            return False
        
        shorter = head1 if len1<len2 else head2
        longer = head2 if len1<len2 else head1
        
        diff = abs(len1-len2)
        
        curr=longer
        for i in range(k):
            if curr:
                curr=curr.next
        longer = curr
        
        while shorter is not longer:
            shorter=shorter.next
            longer=longer.next
            
        return longer ## return any one longer or shorter
        
    def tailAndSize(self,head):
        count=1
        while head.next:
            count+=1
            head=head.next
        return head, count
        
        
        
ll=LinkedList()
ll.head=Node(7)
ll.insert(Node(1))
ll.insert(Node(6))
ll.insert(Node(2))
ll.print_ll()

ll1=LinkedList()
ll1.head=Node(5)
ll1.insert(Node(9))
ll1.insert(Node(2))
ll1.print_ll()

sol=Solution()
sol.intersection(ll.head,ll1.head)
#ll.print_ll()