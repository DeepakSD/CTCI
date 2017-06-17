'''
Created on Jun 9, 2017

@author: deepaks
'''
class Node:
    def __init__(self,data):
        self.val=data
        self.left=None
        self.right=None
        self.leftSize=0

class Solution: 
    def __init__(self):
        self.root=None
    
    def track(self,data):
        if self.root is None:
            self.root=Node(data)
        else:
            self.root=self.insert(self.root,data)
    
    def insert(self,root,data):
        if root is None:
            return Node(data)
        if data <= root.val:
            root.left=self.insert(root.left, data)
            root.leftSize+=1
        else:
            root.right=self.insert(root.right, data)
        return root

    def getRankOfNumber(self,num):
        if self.root is None:
            return None
        return self.getRank(self.root,num)
    
    def getRank(self,root,num):
        if root is None:
            return None
        if num == root.val:
            return root.leftSize
        elif num < root.val:
            return self.getRank(root.left, num)
        else:
            rightSize=self.getRank(root.right, num)
            if rightSize is None:
                return None
            return root.leftSize+1+rightSize
             

sol=Solution()
stream = [ 5, 1, 4, 4, 5, 9, 7, 13, 3 ]
for data in stream:
    sol.track(data)
print sol.getRankOfNumber(9)

            