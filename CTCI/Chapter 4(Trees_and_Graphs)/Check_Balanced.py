'''
Created on May 28, 2017

@author: deepaks
'''
class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def isBalanced(self,root):
        return self.checkHeight(root)!=float('-inf')
    
    def checkHeight(self,root):
        if not root:
            return -1
        leftHeight=self.checkHeight(root.left)
        if leftHeight==float('-inf'):
            return float('-inf')
        
        rightHeight=self.checkHeight(root.right)
        if rightHeight==float('-inf'):
            return float('-inf')
        
        diff=abs(leftHeight-rightHeight)
        if diff>1:
            return float('-inf')
        else:
            return max(leftHeight,rightHeight)+1
        

root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)
#root.right.left.left=Node(25)
sol=Solution()
print sol.isBalanced(root)
