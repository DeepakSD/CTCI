'''
Created on Jun 6, 2017

@author: deepaks
'''
def makeChange(n):
    denoms=[25,10,5,1]
    map=[[-1 for _ in range(len(denoms))] for _ in range(n+1)]
    return makeChangeHelper(n,denoms,0,map)

def makeChangeHelper(amount,denoms,index,map):
    if map[amount][index]>-1:
        return map[amount][index]
    
    if index>=len(denoms)-1:
        return 1
    denomAmount=denoms[index]
    ways=0
    for i in range(amount+1):
        if i*denomAmount<=amount:
            amountRemaining=amount-i*denomAmount
            ways+=makeChangeHelper(amountRemaining, denoms, index+1, map)
    
    map[amount][index]=ways
    return ways

print makeChange(100)