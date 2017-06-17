'''
Created on Jun 10, 2017

@author: deepaks
'''
def setupDictionary(book):
    hmap=dict()
    for word in book:
        word=word.lower()
        if word not in hmap:
            hmap[word]=1
        else:
            hmap[word]+=1
    return hmap

def getFrequency(hmap,word):
    word=word.lower()
    if word=="" or hmap is None:
        return -1
    if word in hmap:
        return hmap[word]
    return 0


book=["the", "Lara", "and", "outcropping", "career", "it"]
dictionary=setupDictionary(book)
print getFrequency(dictionary,"")