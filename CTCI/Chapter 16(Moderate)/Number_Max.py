'''
Created on Jun 11, 2017

@author: deepaks
'''
def getMax(a,b): # Does not handle overflow 
    k=sign(a-b)
    q=flip(k)
    return a*k+b*q
    
def sign(num):
    return flip((num>>63) & 1)

def flip(bit):
    return 1^bit


def getMax1(a,b): #Efficient with overflow
    sa=sign(a)
    sb=sign(b)
    sc=sign(a-b)
    
    use_sign_of_a = sa^sb # If signs are different, then k=sign(a)
    use_sign_of_c = flip(sa^sb) # If sign are same, then k=sign(a-b)
    
    k=sa*use_sign_of_a + sc*use_sign_of_c
    q=flip(k)
    
    return a*k+b*q

print getMax(3,-14)