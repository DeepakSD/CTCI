'''
Created on Mar 23, 2017

@author: deepaks
'''
def palindromePermutation(string):
    dict={}
    #string=string.upper()
    for ch in string:
        if ch!=' ':
           dict[ch]=dict.get(ch,0)+1
    arr=dict.values()
    onecount=0
    for item in arr:
        if item%2!=0:
            onecount+=1
    if onecount>1:
        return False
    return True


def palindromePermutation1(string):
    table = [0 for _ in range(0,(ord('z')-ord('a')+1))]
    oddcount=0
    a=ord('a')
    z=ord('z')
    for ch in string:
        temp=ord(ch)
        if a<=temp<=z:
            table[temp-a]+=1
            if table[temp-a] % 2==1:
                oddcount+=1
            else:
                oddcount-=1
        else:
            return False
    
    return oddcount<=1
    
def palindromePermutation2(string):
    bitvector=0
    for ch in string:
        x=ord(ch)-ord('a')
        bitvector=toggle(bitvector,x)
    
    return bitvector==0 or (bitvector&(bitvector-1))==0
        
        
def toggle(bitvector,index):
    if index<0:
        return bitvector
    
    mask=1<<index
    if bitvector & mask==0:
        bitvector|=mask
    else:
        bitvector&=~mask
    return bitvector
    
    


string="tactco"
print palindromePermutation1(string)