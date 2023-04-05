class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = set()
        self.helper(0,nums,len(nums)-1)
        
        res = []
        for num in self.res:
            temp = []
            ind = 0
            while num:
                if num & 1:
                    temp.append(nums[ind])
                num >>= 1
                ind += 1
            res.append(temp)
        return res         
    
    def helper(self,num,nums,ind):
        if ind >= 0:
            for i in range(ind,-1,-1):
                self.helper(num | (1<<(i)),nums,i-1)
        self.res.add(num)

        
    