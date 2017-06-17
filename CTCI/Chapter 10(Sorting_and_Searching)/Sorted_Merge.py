'''
Created on Jun 8, 2017

@author: deepaks
'''
def merge(arr1,arr2,m,n):
    last1=m-1
    last2=n-1
    finalIndex=m+n-1
    index=finalIndex
    while last2>=0:
        if last1>=0 and arr1[last1]>arr2[last2]:
            arr1[index]=arr1[last1]
            last1-=1
        else:
            arr1[index]=arr2[last2]
            last2-=1
        index-=1
    return arr1[:finalIndex+1]

            

arr1=[9,16,20,None,None,None,None,None,None]
arr2=[1,2,8,12,18,25]
print merge(arr1,arr2,3,len(arr2))