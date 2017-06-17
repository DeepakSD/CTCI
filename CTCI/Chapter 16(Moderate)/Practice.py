'''
Created on Jun 13, 2017

@author: deepaks
'''
class TrieNode:
    def __init__(self):
        self.word=False
        self.children={}
        
    def terminates(self):
        return self.word
        
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node=self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch]=TrieNode()
            node=node.children[ch]
        node.word=True
    
    def getRoot(self):
        return self.root

class Solution:
        t9letters=[None,None,['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
        
        def getValidT9Words(self,number,trie):
            res=[]
            self.getValidWords(number, 0, "", trie.getRoot(), res)
            return res
        
        def getValidWords(self,number,index,prefix,trieNode,res):
            if index==len(number):
                if trieNode.terminates():
                    res.append(prefix)
                return
            
            digit = number[index]
            dig=ord(digit)-ord('0')
            letters=self.t9letters[dig]
            
            if letters is not None:
                for ch in letters:
                    if ch in trieNode.children:
                        child=trieNode.children[ch]
                    else:
                        child=None
                    if child is not None:
                        self.getValidWords(number, index+1, prefix+ch, child, res) 
            

trie=Trie()
trie.insert("tree")
trie.insert("used")
sol=Solution()
print sol.getValidT9Words("8733",trie)