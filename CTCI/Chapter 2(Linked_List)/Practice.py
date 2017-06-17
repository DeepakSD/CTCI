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

class PartialSum:
    def __init__(self):
        self.tot=Node(None)
        self.carry=0
        
class Solution: 
    def sumLists1(self,head1,head2): # Digits in forward order
        len1=self.length(head1)
        len2=self.length(head2)
        
        if len1<len2:
            haed1 = self.padList(head1,len2-len1)
        else:
            head2 = self.padList(head2,len1-len2)
            
        total=self.addHelper(head1,head2)
        if total.carry==0:
            self.display(total.tot)
        else:
            result=self.insertBefore(total.tot,total.carry)
            self.display(result)
            
    def display(self,head):
        while head:
            print head.data,
            head=head.next
        
    def addHelper(self,head1,head2):
        if head1 is None and head2 is None:
            total = PartialSum() 
            return total
        
        total = self.addHelper(head1.next, head2.next)
        val = total.carry+head1.data + head2.data
        
        full_result = self.insertBefore(total.tot, val%10)
        
        total.tot=full_result
        total.carry=val//10
        return total
        
    def padList(self,head,diff):
        for i in range(diff):
            head=self.insertBefore(head,0)
        return head
    
    def insertBefore(self,head,data):
        newNode=Node(data)
        if head is not None:
            newNode.next=head
        return newNode
        
    def length(self,head):
        count=0
        while head:
            count+=1
            head=head.next
        return count
            
            
        
ll=LinkedList()
ll.head=Node(7)
ll.insert(Node(1))
ll.insert(Node(6))
ll.print_ll()

ll1=LinkedList()
ll1.head=Node(5)
ll1.insert(Node(9))
ll1.insert(Node(5))
ll1.print_ll()

sol=Solution()
sol.sumLists1(ll.head,ll1.head)