'''
Created on Jun 8, 2017

@author: deepaks
'''
def searchInRotatedArray(arr,target): # Even array contain duplicates
    return search(arr,0,len(arr)-1,target)

def search(arr,l,r,target):
    mid=(l+r)//2
    if arr[mid]==target:
        return mid
    
    if r<l:
        return -1
    
    if arr[l]<arr[mid]:
        if arr[l]<=target<arr[mid]:
            return search(arr,l,mid-1,target)
        else:
            return search(arr,mid+1,r,target)
    elif arr[l]>arr[mid]:
        if arr[mid]<target<=arr[r]:
            return search(arr,mid+1,r,target)
        else:
            return search(arr,l,mid-1,target)
    
    elif arr[l]==arr[mid]:
        if arr[mid]!=arr[r]: # Search right half
            return search(arr,mid+1,r,target)
        else: 
            result = search(arr,l,mid-1,target) # Search left half
            if result==-1: # If result is None, search right half
                return search(arr,mid+1,r,target)
            else: # Else return result
                return result
        
    return -1


arr=[2,3,4,2,2,2,2]
target=4
print searchInRotatedArray(arr, target)
