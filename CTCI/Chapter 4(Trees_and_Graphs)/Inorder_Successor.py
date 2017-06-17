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
    def inorderSuccessor(self, root):
        succ=None
        p=root.val
        while root:
            if p<root.val:
                succ=root
                root=root.left
            else:
                root=root.right
        return succ.val
        
        
root = Node(9)
root.left = Node(6)
root.right = Node(20)
root.left.left = Node(2)
root.left.right = Node(8)
root.right.left = Node(15)
root.right.right = Node(25)
root.right.right.left = Node(22)
root.right.right.right = Node(30)
sol=Solution()
result=sol.inorderSuccessor(root.right)
print result