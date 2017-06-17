'''
Created on Mar 21, 2017

@author: deepaks
'''
class Solution:
    def isUnique(self,word):
        if len(word)>128:
            return False
        
        boolArray=[False for _ in range(128)]
        for w in word:
            if boolArray[ord(w)]:
                return False
            else:
                boolArray[ord(w)]=True
        return True
    
    def isUnique1(self,word):
        if len(word)>128:
            return False
        
        dict={}
        for w in word:
            if w in dict:
                return False
            else:
                dict[w]=1
        return True
    
sol=Solution()
word="Deepak"
print sol.isUnique1(word)