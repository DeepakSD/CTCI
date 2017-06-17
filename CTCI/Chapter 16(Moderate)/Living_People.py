'''
Created on Jun 13, 2017

@author: deepaks
'''
import random
class  Person:
    def __init__(self,birthYear,deathYear):# Time Complexity O(P+R) where R is the range of years
        self.birth=birthYear
        self.death=deathYear

def maxAliveYear(people,mini,maxi):
    years=getPopulationDeltas(people,mini,maxi)
    maxYear=getMaxAlive(years)
    return maxYear+mini

def getPopulationDeltas(people,mini,maxi):
    years=[0]*(maxi-mini+2)
    for ppl in people:
        years[ppl.birth-mini]+=1
        years[ppl.death-mini+1]-=1
    return years

def getMaxAlive(years):
    currentlyAlive=0
    maxAlive=0
    yearIndex=0
    for idx,element in enumerate(years):
        currentlyAlive+=element
        if currentlyAlive>maxAlive:
            maxAlive=currentlyAlive
            yearIndex=idx
    return yearIndex



n = 100
first = 1900
last = 2000
people=[]
for i in range(n):
    birth = first + random.randint(0,last-first)
    death = birth + random.randint(0,last-birth)
    print birth,death
    people.append(Person(birth, death))
    
print maxAliveYear(people, first, last)

