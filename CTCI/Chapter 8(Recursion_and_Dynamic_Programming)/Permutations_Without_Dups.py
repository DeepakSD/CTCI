'''
Created on May 31, 2017

@author: deepaks
'''
def permutation(string):
    res=[]
    permutationAll(string,"",res)
    return res

def permutationAll(remainder,prefix,res):
    if len(remainder)==0:
        res.append(prefix)
    
    else:
        for i in range(0,len(remainder)):
            remaining=remainder[:i]+remainder[i+1:]
            permutationAll(remaining,prefix+remainder[i],res)
            
print permutation("sum") # String must contain only unique characters