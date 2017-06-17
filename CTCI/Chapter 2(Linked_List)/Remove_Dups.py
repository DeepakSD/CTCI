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
    def removeDups(self,head):## With buffer # O(n) time but O(n) space
        curr=head
        seen=set([curr.data])
        while curr.next:
            if curr.next.data in seen:
                curr.next=curr.next.next
            else:
                seen.add(curr.next.data)
                curr=curr.next
        return head
    
    def removeDups_FollowUp(self,head):## Without any buffer # O(n^2) time but O(1) space
            curr=head
            while curr:
                runner=curr
                while runner.next:
                    if runner.next.data==curr.data:
                        runner.next=runner.next.next
                    else:
                        runner=runner.next
                curr=curr.next
            return head
        
        
        
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
#ll.head=sol.removeDups(ll.head)
ll.head=sol.removeDups_FollowUp(ll.head)
ll.print_ll()