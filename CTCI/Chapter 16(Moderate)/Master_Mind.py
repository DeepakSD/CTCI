'''
Created on Jun 14, 2017

@author: deepaks
'''
def estimate(guess,solution):
    codeMap={'B':0,'R':1,'G':2,'Y':3}
    if len(guess)!=len(solution):
        return None
    frequencies=[0]*len(codeMap)
    hits=0
    for i in range(len(guess)):
        if guess[i]==solution[i]:
            hits+=1
        else:
            code=codeMap[solution[i]]
            frequencies[code]+=1
    
    pseudo_hits=0
    for i in range(len(guess)):
        code=codeMap[guess[i]]
        if code>=0 and frequencies[code]>0 and guess[i]!=solution[i]:
            pseudo_hits+=1
            frequencies[code]-=1
    return hits,pseudo_hits

guess="RGBY"
solution="GGRB"
print estimate(guess,solution)