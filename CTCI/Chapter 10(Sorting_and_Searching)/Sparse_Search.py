'''
Created on Jun 8, 2017

@author: deepaks
'''
def sparseSearch(strings,target):
    if strings is None or target is None or target=="":
        return -1
    return search(strings,target,0,len(strings)-1)

def search(strings,target,l,r):
    if r<l:
        return -1
    
    mid=(l+r)//2
    if strings[mid]=="":
        left=mid-1
        right=mid+1
        while True:
            if left<l or right>r:
                return -1
            elif left>=l and strings[left]!="":
                mid=left
                break
            elif right<=r and strings[right]!="":
                mid=right
                break
            left-=1
            right+=1
        
    if strings[mid]==target:
        return mid
    elif strings[mid]<target:
        return search(strings,target,mid+1,r)
    else:
        return search(strings,target,l,mid-1)


strings=["at","","","","ball","","","car","","","dad","",""]
target="ball"
print sparseSearch(strings, target)