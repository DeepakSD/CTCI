'''
Created on Jun 3, 2017

@author: deepaks
'''
def countWays(n):
    memo=[-1]*(n+1)
    return countWaysHelper(n,memo)

def countWaysHelper(n,memo):
    if n<0:
        return 0
    elif n==0:
        return 1
    elif memo[n]>-1:
        return memo[n]
    else:
        memo[n]=countWaysHelper(n-1, memo) + countWaysHelper(n-2, memo) + countWaysHelper(n-3, memo)
        return memo[n]
    

print countWays(39)