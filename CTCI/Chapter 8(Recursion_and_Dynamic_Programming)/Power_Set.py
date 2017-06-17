'''
Created on Jun 5, 2017

@author: deepaks
'''
class Solution:
    def subsets(self,nums):
        res=[]
        self.dfs(nums,[],res,0)
        return res
    
    def dfs(self,nums,path,res,index):
        res.append(path)
        for i in range(index,len(nums)):
            self.dfs(nums, path+[nums[i]],res,i+1)
            
    
    def subsets1(self, nums):####Iterative Solution
        res = [[]]
        nums.sort()
        for i in range(len(nums)):
            for j in range(0, len(res)):
                res.append(res[j] + [nums[i]])
        return res
 

nums=[1,2,3]   
sol=Solution()
print sol.subsets(nums)