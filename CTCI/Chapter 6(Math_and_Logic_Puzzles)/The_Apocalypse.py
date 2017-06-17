'''
Created on Jun 1, 2017

@author: deepaks
'''
import random
def runNFamilies(n):
    boys=0
    girls=0
    for _ in range(n):
        genders=runOneFamily()
        girls+=genders[1]
        boys+=genders[0]
    return girls/float(boys+girls)
        
        
def runOneFamily():
    boys=0
    girls=0
    while girls==0:
        if random.choice([True,False]):
            girls+=1
        else:
            boys+=1
    return [boys,girls]


print runNFamilies(100)
    