'''
Created on Jun 16, 2017

@author: deepaks
'''

# Deduction Part
# sumA-a+b = sumB-b+a
# 2a-2b = sumA-sumB
# a-b = (sumA-sumB)/2

def sumSwap(arr1,arr2): # O(A+B)
    target = getTarget(arr1,arr2)
    if target is None:
        return None
    return findDifference(arr1,arr2,target)

def findDifference(arr1,arr2,target):
    contents=set(arr2)
    for one in arr1:
        two=one-target
        if two in contents:
            return (one,two)
    return None
        
    
def getTarget(arr1,arr2):
    sum1=sum(arr1)
    sum2=sum(arr2)
    
    if (sum1-sum2)%2!=0:
        return None
    return (sum1-sum2)/2


arr1=[4,1,2,1,1,2]
arr2=[3,6,3,3]
print sumSwap(arr1,arr2)