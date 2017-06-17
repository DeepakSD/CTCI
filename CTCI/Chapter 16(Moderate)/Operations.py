'''
Created on Jun 13, 2017

@author: deepaks
'''
#Subtraction
def subtraction(a,b): # Time complexity O((log a)^2)
    return a+ negate(b)

def negate(num):
    neg=0
    sign=1 if num<0 else -1
    delta = sign
    while num!=0:
        differentSigns= (num+delta>0) != (num>0)
        if num+delta!=0 and differentSigns:
            delta = sign
        
        neg+=delta
        num+=delta
        delta+=delta
    return neg

print subtraction(9,5)

#Multiplication
def multiplication(a,b):
    if a<b:
        return multiplication(b,a)
    
    sum=0
    i=absolute(b)
    while i>0:
        sum+=a
        i=subtraction(i,1)
    
    if b<0:
        sum = negate(sum)
    
    return sum
    
def absolute(num):
    if num<0:
        return negate(num)
    else:
        return num

print multiplication(-2,-3)

#Division
def division(a,b):
    if b==0:
        return "Error"
    abs_a = absolute(a)
    abs_b = absolute(b)
    
    product=0
    x=0
    while product+abs_b <= abs_a:
        product+=abs_b
        x+=1
    
    if (a<0 and b<0) or (a>0 and b>0):
        return x
    else:
        return negate(x)
        
print division(3,9)

