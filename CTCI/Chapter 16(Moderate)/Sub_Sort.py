'''
Created on Jun 14, 2017

@author: deepaks
'''
def findUnsortedSequence(arr):
    leftEnd = findEndofLeftSubsequence(arr)
    if leftEnd>=len(arr)-1:
        return "Already sorted"
    
    rightStart = findStartofRightSubsequence(arr)
    
    maxIndex=leftEnd
    minIndex=rightStart
    for i in range(leftEnd+1,rightStart):
        if arr[i]<arr[minIndex]:
            minIndex=i
        if arr[i]>arr[maxIndex]:
            maxIndex=i

    
    leftIndex = shrinkLeft(arr,minIndex,leftEnd)
    rightIndex = shrinkRight(arr,maxIndex,rightStart)
    
    return leftIndex,rightIndex
    
    
def findEndofLeftSubsequence(arr):
    for i in range(1,len(arr)):
        if arr[i]<arr[i-1]:
            return i-1
    return len(arr)-1

def findStartofRightSubsequence(arr):
    for i in range(len(arr)-2,-1,-1):
        if arr[i]>arr[i+1]:
            return i+1
    return 0

def shrinkLeft(arr,minIndex,start):
    comp = arr[minIndex]
    for i in range(start-1,-1,-1):
        if arr[i]<=comp:
            return i+1
    return 0

def shrinkRight(arr,maxIndex,start):
    comp = arr[maxIndex]
    for i in range(start,len(arr)):
        if arr[i]>=comp:
            return i-1
    return len(arr)-1


arr=[1,2,4,7,10,11,7,17,6,12,6,7,16,18,19]
print findUnsortedSequence(arr) 
     