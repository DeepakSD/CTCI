'''
Created on Jun 8, 2017

@author: deepaks
'''
def search(arr,value):
    index=1
    while arr[index]!=-1 and arr[index]<value:
        index*=2
    return binarySearch(arr,value,index/2,index)

def binarySearch(arr,value,l,r):
    while l<=r:
        mid=(l+r)//2
        middle=arr[mid]
        if middle>value or middle==-1:
            r=mid-1
        elif middle<value:
            l=mid+1
        else:
            return mid
    return -1

arr=[1,5,6,7,8,9,10,15,18,19,27,29,45,57]
target=19
print search(arr,target)