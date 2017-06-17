'''
Created on Mar 22, 2017

@author: deepaks
'''
def URLify(string,length):
    string=list(string)
    for i in range(length):
        if string[i]==" ":
            string[i]="%20"
    return "".join(string)

def URLify1(string,length):
    string=list(string)
    spaceCount=0
    for i in range(length):
        if string[i]==" ":
            spaceCount+=1
    
    index=length+spaceCount*2
    if length<len(string):
        string[length]='\0'
    for i in reversed(range(length)):
        if string[i]==" ":
            string[index-1]="0"
            string[index-2]="2"
            string[index-3]="%"
            index-=3
        else:
            string[index-1]=string[i]
            index-=1
    return "".join(string)

def URLify2(string, length):####Perfect Solution
    new_index = len(string)
    string=list(string)

    for i in reversed(range(length)):
        if string[i] == ' ':
            # Replace spaces
            string[new_index - 3:new_index] = '%20'
            new_index -= 3
        else:
            # Move characters
            string[new_index - 1] = string[i]
            new_index -= 1

    return "".join(string)

string="much ado about nothing      "
strlength=22
print URLify2(string,strlength)