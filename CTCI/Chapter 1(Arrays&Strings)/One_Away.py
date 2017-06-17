'''
Created on Apr 3, 2017

@author: deepaks
'''
import math
def oneAway(first,second):###Best Solution
    i=0
    while i<min(len(first),len(second)) and first[i]==second[i]:
        i+=1
    if not (i==len(first)==len(second)) and first[i+(len(first)>=len(second)):]==second[i+(len(first)<=len(second)):]:
        return True
    return False
    
    
def oneAway1(first,second):
    if len(first)==len(second):
        return replaceCheck(first,second)
    elif len(first)+1==len(second) or len(first)-1==len(second):
        string1=first if len(first)<len(second) else second
        string2=second if len(first)<len(second) else first
        return insdelCheck(string1,string2)
    return False


def replaceCheck(first,second):
    oneEdit=0
    for i in range(0,len(first)):
        if first[i]!=second[i]:
            oneEdit+=1
    return oneEdit==1

def insdelCheck(first,second):
    index1=0
    index2=0
    while index2<len(second) and index1<len(first):
        if first[index1]!=second[index2]:
            if index1!=index2:
                return False
            index2+=1
        else:
            index1+=1
            index2+=1
    return True


def oneAway2(string1,string2):
    if abs(len(string1)-len(string2))>1:
        return False
    first=string1 if len(string1)<len(string2) else string2
    second=string2 if len(string1)<len(string2) else string1
    index1=0
    index2=0
    foundDifference=False
    while index2<len(second) and index1<len(first):
        if first[index1]!=second[index2]:
            if foundDifference:
                return False
            foundDifference=True
                
            if len(first)==len(second):
                index1+=1
        else:
            index1+=1
        index2+=1
    return True

        
        

first="pale"
second="ple"
print oneAway(first,second)