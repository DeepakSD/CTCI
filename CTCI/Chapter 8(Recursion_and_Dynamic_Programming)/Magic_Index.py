'''
Created on Jun 5, 2017

@author: deepaks
'''
def magicIndex(arr):
    return findIndex1(arr,0,len(arr)-1)

def findIndex(arr,l,r):## When array elements are distinct
    if r<l:
        return -1
    
    mid=(l+r)//2
    if arr[mid]==mid:
        return mid
    elif arr[mid]<mid:
        return findIndex(arr,mid+1,r)
    else:
        return findIndex(arr, l, mid-1)
    
def findIndex1(arr,l,r):## When array elements are not distinct
    if r<l:
        return -1
    
    mid=(l+r)//2
    midValue=arr[mid]
    if mid==midValue:
        return mid
    
    leftIndex=min(mid-1,midValue)
    left=findIndex1(arr, l, leftIndex)
    if left>=0:
        return left
    
    rightIndex=max(mid+1,midValue)
    right=findIndex1(arr, rightIndex, r)
    
    return right

arr=[-10,-5,2,2,2,3,4,7,9,12,13]
print magicIndex(arr)
