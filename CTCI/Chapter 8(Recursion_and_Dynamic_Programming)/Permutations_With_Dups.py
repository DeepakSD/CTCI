'''
Created on Jun 6, 2017

@author: deepaks
'''
def permutation(string):
    res=[]
    hmap=buildFreqTable(string)
    permutationAll(hmap,"",len(string),res)
    return res

def buildFreqTable(string):
    hmap=dict()
    for ch in string:
        if ch not in hmap:
            hmap[ch]=1
        else:
            hmap[ch]+=1
    return hmap

def permutationAll(hmap,prefix,remainder,res):
    if remainder==0:
        res.append(prefix)

    for k,count in hmap.items():
        if count>0:
            hmap[k]=count-1
            permutationAll(hmap,prefix+k,remainder-1,res)
            hmap[k]=count
            
print permutation("sum")