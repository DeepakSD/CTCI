'''
Created on May 29, 2017

@author: deepaks
'''
class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
def pathsWithSum(root,targetSum):
    if root is None:
        return 0
    hmap={0:1}
    return sumHelper(root,targetSum,0,hmap)

def sumHelper(root,targetSum,runningSum,hmap):
    if root is None:
        return 0
    runningSum+=root.val
    try:
        hmap[runningSum]+=1
    except KeyError:
        hmap[runningSum]=1
    try:
        totalPaths=hmap[runningSum-targetSum]
    except KeyError:
        totalPaths=0
    
    totalPaths+=sumHelper(root.left, targetSum, runningSum, hmap)
    totalPaths+=sumHelper(root.right, targetSum, runningSum, hmap)
    hmap[runningSum]-=1
    return totalPaths
    
    
        
        

root = Node(10)
root.left = Node(5)
root.right = Node(-3)
root.left.left = Node(3)
root.left.right = Node(1)
#root.right.left = Node(1)
root.right.right = Node(11)
#root.right.right.left = Node(22)
#root.right.right.right = Node(30)
root.left.left.left=Node(3)
root.left.left.right=Node(-2)
root.left.right.right = Node(2)
targetSum=8
print pathsWithSum(root,targetSum)