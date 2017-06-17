'''
Created on Jun 5, 2017

@author: deepaks
'''
def minProduct(a,b):
    smaller = a if a<b else b
    bigger = b if a<b else a
    memo=[-1]*(smaller+1)
    return minProductHelper1(smaller,bigger)

def minProductHelper(smaller,bigger,memo):
    if smaller==0:
        return 0
    elif smaller==1:
        return bigger
    elif memo[smaller]>0:
        return memo[smaller]
    
    s=smaller>>1 # divide by 2
    side1=minProductHelper(s, bigger,memo)
    side2=side1
    if smaller%2==1:
        side2=minProductHelper(smaller-s, bigger,memo)
    
    memo[smaller]=side1+side2
    return side1+side2

def minProductHelper1(smaller,bigger): # Bit faster than above solution
    if smaller==0:
        return 0
    elif smaller==1:
        return bigger

    s=smaller>>1 # divide by 2
    halfProd=minProductHelper1(s, bigger)

    if smaller%2==0:
        return halfProd+halfProd
    else:
        return halfProd+halfProd+bigger
    

print minProduct(7, 8)