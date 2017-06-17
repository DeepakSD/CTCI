'''
Created on Apr 19, 2017

@author: deepaks
'''
def isSubstring(string,sub):
    for i in range(len(string)):
        if string[i:i+len(sub)]==sub:
            return True
    return False

def isRotation(s1,s2):
    if len(s1)==len(s2):
        return isSubstring(s1+s1,s2)
    return False
    

s1="waterbottle"
s2="erbottlewat"
print isRotation(s1, s2)