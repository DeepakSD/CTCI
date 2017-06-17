'''
Created on Jun 16, 2017

@author: deepaks
'''
def doesMatch(value,pattern): #Brute force Algorithm O(n^4)
    size=len(value)
    for i in range(size):
        main=value[0:i]
        for altStart in range(i,size+1):
            for altEnd in range(altStart,size+1):
                alt=value[altStart:altEnd]
                res=buildPattern(pattern,main,alt) 
                if res==value:
                    print main, alt
                    return True
    return False
    
def buildPattern(pattern,main,alt):
    res=[]
    first=pattern[0]
    for ch in pattern:
        if ch==first:
            res.append(main)
        else:
            res.append(alt)
    return "".join(res)

def doesMatch1(value,pattern):
    if len(pattern)==0:
        return len(value)==0
    
    mainChar = pattern[0]
    altChar = 'b' if mainChar=='a' else 'a'
    size = len(value)
    
    countOfMain = countOf(pattern,mainChar)
    countOfAlt = len(pattern) - countOfMain
    firstAlt = pattern.index(altChar)
    maxMainSize = size/countOfMain
    
    for i in range(maxMainSize+1):
        remainingLength = size-i*countOfMain
        first = value[0:i]
        if countOfAlt==0 or remainingLength%countOfAlt==0:
            altIndex = firstAlt*i
            altSize = 0 if countOfAlt==0 else remainingLength/countOfAlt
            second = "" if countOfAlt==0 else value[altIndex:altIndex+altSize]
            
            res=buildPattern(pattern, first, second)
            if res==value:
                print first,second
                return True
    return False
    
def countOf(pattern,c):
    count=0
    for i in range(len(pattern)):
        if pattern[i]==c:
            count+=1
    return count

print doesMatch1("catcatgocatgo","aabab")