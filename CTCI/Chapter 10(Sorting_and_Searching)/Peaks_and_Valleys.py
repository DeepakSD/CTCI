'''
Created on Jun 9, 2017

@author: deepaks
'''
def sortValleyPeak(arr):
    i=1
    while i<len(arr):
        biggestIndex=maxIndex(arr,i-1,i,i+1)
        if i!=biggestIndex:
            arr[i],arr[biggestIndex]=arr[biggestIndex],arr[i]
        i+=2
    return arr

def maxIndex(arr,a,b,c):
    length=len(arr)
    aValue=arr[a] if a>=0 and a<length else float("-inf")
    bValue=arr[b] if b>=0 and b<length else float("-inf")
    cValue=arr[c] if c>=0 and c<length else float("-inf")
    
    maxi=max(aValue,max(bValue,cValue))
    if aValue==maxi:
        return a
    elif bValue==maxi:
        return b
    else:
        return c
    
arr=[9,1,0,4,8,7]
print sortValleyPeak(arr)