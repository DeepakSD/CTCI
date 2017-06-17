'''
Created on Jun 10, 2017

@author: deepaks
'''
def numberSwapper(num1,num2): # Without using temp variable
    
    num1 = num1 ^ num2
    num2 = num1 ^ num2
    num1 = num1 ^ num2
    
    return num1,num2

def numberSwapper(num1,num2): # Without using temp variable ## Only for integers
    
    num1 = num1 - num2
    num2 = num1 + num2
    num1 = num2 - num1
    
    return num1,num2

print numberSwapper(6, 9)