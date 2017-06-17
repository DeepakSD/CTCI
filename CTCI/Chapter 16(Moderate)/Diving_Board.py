'''
Created on Jun 13, 2017

@author: deepaks
'''
def allLengths(k,shorter,longer): #Memoization # Runtime: O(K^2)
    lengths=set()
    visited=set()
    helper(k,0,shorter,longer,lengths,visited)
    return lengths

def helper(k,total,shorter,longer,lengths,visited):
    if k==0:
        lengths.add(total)
        return
    
    key=str(k)+" "+str(total)
    if key in visited:
        return
    
    helper(k-1,total+shorter,shorter,longer,lengths,visited)
    helper(k-1,total+longer,shorter,longer,lengths,visited)
    visited.add(key)

def allLengths1(k,shorter,longer): # Optimized Solution
    lengths=set()
    for nshorter in range(k+1):
        nlonger=k-nshorter
        length=nshorter*shorter + nlonger*longer
        lengths.add(length)
    return lengths

nSticks=12
shorter=2
longer=3
print allLengths(nSticks,shorter,longer)