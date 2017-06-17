'''
Created on May 28, 2017

@author: deepaks
'''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
                    
class Solution:
    def isValidBST(self, root):
        return self.check(root,float('-inf'),float('inf'))
        
    def check(self,root,mini,maxi):
        if root is None:
            return True
        
        if root.val<=mini or root.val>maxi:
            return False
        
        return self.check(root.left,mini,root.val) and self.check(root.right,root.val,maxi)
            
        
    

            
root=TreeNode(6)
root.left=TreeNode(4)
root.right=TreeNode(8)
root.left.left=TreeNode(3)
root.left.right=TreeNode(6)
sol=Solution()
print sol.isValidBST(root)
