'''
Created on May 28, 2017

@author: deepaks
'''
from math import floor
from random import random
class Node:
    def __init__(self,data):
        self.val=data
        self.left=None
        self.right=None
        self.size=1
     
class Solution: 
    root=None  
    def insert(self,node):
        if self.root is None:
            self.root=node
        else:
            self.insertInorder(self.root,node)
            
    def insertInorder(self,root,node):
        if root.val > node.val:
            if root.left is None:
                root.left=node
            else:
                self.insertInorder(root.left,node)
        else:
            if root.right is None:
                root.right = node
            else:
                self.insertInorder(root.right, node)
        root.size+=1
    
    def delete(self,data):
        return self.deleteNode(self.root,data)
    
    def deleteNode(self,root,data):
        if not root:
            return root
        if data < root.val:
            root.left=self.deleteNode(root.left, data)
        elif data>root.val:
            root.right=self.deleteNode(root.right, data)
        
        else:
            if root.left is None:
                temp=root.right
                root=None
                return temp
            
            elif root.right is None:
                temp=root.left
                root=None
                return temp
            else:
                succ=root.right
                while succ.left:
                    succ=succ.left
                
                root.val = succ.val
                root.right = self.deleteNode(root.right, succ.val)
                
        root.size-=1
        return root
        
    def find(self,data):
        if self.root is None:
            return None
        else:
            return self.search(self.root,data)
    
    def search(self,root,data):
        if root.val==data:
            return root
        if root.left and root.val>data:
            return self.search(root.left, data)
        elif root.right and root.val<data:
            return self.search(root.right, data)
        else:
            return None
        
    def randomNode(self):
        if self.root is None:
            return None
        else:
            return self.getRandomNode(self.root)
        
    def getRandomNode(self,root):
        if root.left:
            sizeLeft=root.left.size
        else:
            sizeLeft=0
        index=floor(root.size*random())
        if index<sizeLeft:
            return self.getRandomNode(root.left)
        elif index==sizeLeft:
            return root.val
        else:
            return self.getRandomNode(root.right)
        
sol=Solution()
sol.insert(Node(9))
sol.insert(Node(6))
sol.insert(Node(20))
sol.insert(Node(15))
sol.insert(Node(25))
sol.insert(Node(22))
sol.insert(Node(30))
print sol.randomNode()
print sol.find(20)
root=sol.delete(25)
        