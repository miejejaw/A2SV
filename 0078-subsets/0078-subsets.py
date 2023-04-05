class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = set()
        self.length = len(nums)
        self.helper(0,nums,0)
        return self.h(self.res,nums)
         
    
    def helper(self,num,nums,ind):
        if ind < self.length:
            for i in range(ind,self.length):
                self.helper(num | (1<<(i)),nums,i+1)
        self.res.add(num)
        
    def h(self,s,nums):
        res = []
        for num in s:
            temp = []
            ind = 0
            while num:
                if num & 1:
                    temp.append(nums[ind])
                num >>= 1
                ind += 1
            res.append(temp)
        return res
        
    