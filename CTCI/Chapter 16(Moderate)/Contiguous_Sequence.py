'''
Created on Jun 14, 2017

@author: deepaks
'''
def getMaxSum(arr):
    maxSum=0
    tot=0
    for element in arr:
        tot+=element
        if tot>maxSum:
            maxSum=tot
        elif tot<0:
            tot=0
    return maxSum

arr=[2,-8,3,-2,4,-10]
print getMaxSum(arr) 