'''
Created on Jun 10, 2017

@author: deepaks
'''
def countFactZeros(num): #Efficient Algorithm
    count=0
    if num<0:
        return -1
    i=5
    while num/i>0:
        count+=num/i
        i*=5
    return count

def countFactZeros1(num): # Using factors of 5 separate function
    i=2
    count=0
    while i<=num:
        count+=factorOf5(i)
        i+=1
    return count

def factorOf5(num):
    count=0
    while num%5==0:
        count+=1
        num/=5
    return count

print countFactZeros1(19)
     