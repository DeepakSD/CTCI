'''
Created on Jun 11, 2017

@author: deepaks
'''
def findSmallestDifference(arr1,arr2): #O(a log_a + b log_b)
    arr1.sort()
    arr2.sort()
    i=0
    j=0
    res=float("inf")
    while i<len(arr1) and j<len(arr2):
        if abs(arr1[i]-arr2[j])<res:
            res=abs(arr1[i]-arr2[j])
        
        if arr1[i]<arr2[j]:
            i+=1
        else:
            j+=1
    return res


arr1=[1,3,15,11,2]
arr2=[23,127,235,19,8]
print findSmallestDifference(arr1, arr2)