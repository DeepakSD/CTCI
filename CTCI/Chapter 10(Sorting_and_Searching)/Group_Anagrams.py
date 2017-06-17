'''
Created on Jun 8, 2017

@author: deepaks
'''
def groupAnagrams(strings):
    hmap=dict()
    for string in strings:
        temp = tuple(sorted(string))
        if temp not in hmap:
            hmap[temp]=[string]
        else:
            hmap[temp].append(string)
    index=0
    for k,values in hmap.items():
        for v in values:
            strings[index]=v
            index+=1
    return strings
    


strings=["eat", "tea", "tan", "ate", "nat", "bat"]
print groupAnagrams(strings)