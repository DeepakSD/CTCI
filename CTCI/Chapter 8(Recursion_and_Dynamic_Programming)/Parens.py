'''
Created on Jun 6, 2017

@author: deepaks
'''
def generateParens(n):
    if not n:
        return []
    left,right,res=n,n,[]
    dfs(left,right,res,"")
    return res

def dfs(left,right,res,string):
    if right<left:
        return 
    
    if not left and not right:
        res.append(string)
        return
    
    if left:
        dfs(left-1,right,res,string+"(")
    if right:
        dfs(left,right-1,res,string+")")


print generateParens(3)
        