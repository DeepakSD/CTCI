'''
Created on Jun 11, 2017

@author: deepaks
'''
class Solution:
    def __init__(self):
        self.lessThan20=["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        self.tens=["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        self.thousands=["","Thousand","Million","Billion"]
        self.negative="Negative "
        
    
    def numberToWords(self, num):
        if num==0:
            return "Zero"
        elif num<0:
            return self.negative  + self.numberToWords(-1*num)
        res=""
        for i in range(len(self.thousands)):
            if num%1000!=0:
                res=self.helper(num%1000) + self.thousands[i] + " " + res
            num/=1000
        return res.strip()
    
    def helper(self,num):
        if num==0:
            return "Zero"
        elif num<20:
            return self.lessThan20[num] + " "
        elif num<100:
            return self.tens[num/10] + " " + self.helper(num%10)
        else:
            return self.lessThan20[num/100] + " Hundred " + self.helper(num%100) 

num=-8996123   
sol=Solution()
print sol.numberToWords(num)