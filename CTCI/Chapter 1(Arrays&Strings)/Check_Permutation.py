'''
Created on Mar 22, 2017

@author: deepaks
'''
def checkPermutation(string1,string2):
    if len(string1)!=len(string2):
        return False
    dict={}
    for ch in string1:
        if ch not in dict:
            dict[ch]=1
        else:
            dict[ch]+=1
    for ch in string2:
        if dict[ch]==0:
            return False
        dict[ch]-=1
        
    return True

def checkPermutation1(string1,string2):
    if len(string1)!=len(string2):
        return False
    check=0
    for i in range(len(string1)):
        check ^= ord(string1[i]) ^ ord(string2[i])
    
    return check==0


string1="deepak"
string2="eekdah"
print checkPermutation1(string1,string2)