'''
Created on May 28, 2017

@author: deepaks
'''
class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution:
    def areIdentical(self,root1,root2):
        if root1 is None and root2 is None:
            return True
        
        if root1 is None or root2 is None:
            return False
        
        return (root1.val==root2.val and self.areIdentical(root1.left, root2.left) and self.areIdentical(root1.right, root2.right))
        
    def isSubtree(self, s, t):        
        if t is None:
            return True
        if s is None:
            return False
        
        if self.areIdentical(s,t):
            return True
        return self.areIdentical(s.left,t) or self.areIdentical(s.right,t)
    

root1=TreeNode(26)
root1.left=TreeNode(10)
root1.right=TreeNode(3)
root1.left.left=TreeNode(4)
root1.left.right=TreeNode(6)
root1.right.right=TreeNode(3)
root1.left.left.right=TreeNode(30)

root2=TreeNode(10)
root2.left=TreeNode(4)
root2.right=TreeNode(6)
root2.left.right=TreeNode(30)

sol=Solution()
print sol.isSubtree(root1,root2)