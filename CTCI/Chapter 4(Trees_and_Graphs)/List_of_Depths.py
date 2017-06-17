'''
Created on May 28, 2017

@author: deepaks
'''
class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution: # Refer Level Order Traversal in LeetCode
    def levelOrder(self,root):
        res=[]
        self.dfs(root,0,res)
        return res
    
    def dfs(self,root,height,res):
        if not root:
            return None
        
        if height>=len(res):
            res.append([])
        
        res[height].append(root.val)
        self.dfs(root.left, height+1, res)
        self.dfs(root.right, height+1, res)
        
    def levelOrder1(self,root):
        res=[[root.val]]
        queue=[root]
        while len(queue)>0:
            newQueue=[]
            for n in queue:
                if n.left is not None:
                    newQueue.append(n.left)
                if n.right is not None:
                    newQueue.append(n.right)
            queue=newQueue
            if len(queue)!=0:
                res.append([x.val for x in queue])
        return res
             

root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)
sol=Solution()
result=sol.levelOrder1(root)
print result