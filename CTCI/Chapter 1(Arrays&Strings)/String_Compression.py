'''
Created on Apr 3, 2017

@author: deepaks
'''
def stringCompression(string):
    count=0
    res=[]
    for i in range(0,len(string)):
        if string[i]!=string[i-1] and i!=0:
            res.append(string[i-1]+str(count))
            count=0
        count+=1
    res.append(string[-1]+str(count))
    return min(string,''.join(res),key=len)
            
            



string="aabbbccccdd"
print stringCompression(string)