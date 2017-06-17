'''
Created on May 28, 2017

@author: deepaks
'''
class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        

class Solution:
    def firstCommonAncestor(self, root, p, q):
        if not self.isPresent(root,p) or not self.isPresent(root,q):
            return "Node is not found in the tree" 
        return self.findAncestor(root,p,q)
        
        
    def findAncestor(self,root,p,q):    
        if root is None or root.val in (p,q):
            return root
        left=self.findAncestor(root.left, p, q)
        right=self.findAncestor(root.right, p, q)
        if left and right:
            return root.val
        return left or right
    
    def isPresent(self,root,val):
        if root.val==val:
            return True
        found=False    
        if root.left:
            found=self.isPresent(root.left, val) 
        if not found and root.right:
            found=self.isPresent(root.right, val)
        return found
    
root = Node(9)
root.left = Node(6)
root.right = Node(20)
root.left.left = Node(2)
root.left.right = Node(8)
root.right.left = Node(15)
root.right.right = Node(25)
root.right.right.left = Node(22)
root.right.right.right = Node(30)
p=22
q=6
sol=Solution()
print sol.firstCommonAncestor(root, p, q)