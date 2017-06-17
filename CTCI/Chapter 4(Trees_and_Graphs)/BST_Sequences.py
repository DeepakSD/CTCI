'''
Created on May 28, 2017

@author: deepaks
'''
class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
def weave(arr1,arr2,prefix,result):
        if not arr1 or not arr2:
            result.append(prefix+arr1+arr2)
            return result
        
        h1=arr1.pop(0)
        prefix+=[h1]
        weave(arr1,arr2,prefix,result)
        arr1.insert(0,h1)
        prefix.pop()
        
        h2=arr2.pop(0)
        prefix+=[h2]
        weave(arr1,arr2,prefix,result)
        arr2.insert(0,h2)
        prefix.pop()
        return result
        
        
def bstSequence(root):
    if not root:
        return []
    
    if not root.left and not root.right:
        return [[root.val]]
    
    res=[]
    left=bstSequence(root.left)
    right=bstSequence(root.right)
    
    if left and right:
        for left_seq in left:
            for right_seq in right:
                suffix=weave(left_seq,right_seq,[],[])
                res+=[[root.val]+seq for seq in suffix]
    else:
        remaining=left or right
        res+=[[root.val]+seq for seq in remaining]
    return res
        
        

root = Node(9)
root.left = Node(6)
root.right = Node(20)
root.left.left = Node(2)
root.left.right = Node(8)
# root.right.left = Node(15)
# root.right.right = Node(25)
# root.right.right.left = Node(22)
# root.right.right.right = Node(30)
print bstSequence(root)