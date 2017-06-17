'''
Created on May 28, 2017

@author: deepaks
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Solution:
    def minimalTree(self,arr):
        return self.constructBST(arr,0,len(arr)-1)
        
    def constructBST(self,arr,start,end):
        if end<start:
            return None
        
        mid=(start+end)//2
        
        root = Node(arr[mid])
        root.left=self.constructBST(arr, start,mid-1)
        root.right=self.constructBST(arr,mid+1, end)
        
        return root
    
    def printTree(self,root):
        if root:
            self.printTree(root.left)
            print root.data,
            self.printTree(root.right)
    

arr=[1,2,3,4,5,6,7,8,9,10,12,15,18,22,43,144,515]
sol=Solution()
root = sol.minimalTree(arr)
sol.printTree(root)
