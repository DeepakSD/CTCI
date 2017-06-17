'''
Created on May 28, 2017

@author: deepaks
'''
import collections
class Solution:
    def buildOrder(self, projects, dependencies): # Refer Course Schedule II
        hmap=collections.defaultdict(set)
        neigh=collections.defaultdict(set)
        for i,j in dependencies:
            hmap[j].add(i)
            neigh[i].add(j)
        stack=[i for i in projects if not hmap[i]]
        res=[]
        while stack:
            node=stack.pop()
            res.append(node)
            for i in neigh[node]:
                hmap[i].remove(node)
                if not hmap[i]:
                    stack.append(i)
            hmap.pop(node)
        return res if not hmap else []
    
    

projects=['a','b','c','d','e','f']
dependencies=[['a','d'],['f','b'],['b','d'],['f','a'],['d','c']]
sol=Solution()
print sol.buildOrder(projects, dependencies)