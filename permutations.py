class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        self.res = []
        self.length = len(nums)
        self.backtrack(nums,[],0,0)
        return self.res
    
    def backtrack(self,nums,arr,num,ind):
        if ind < self.length:
            for i in range(self.length):
                if not (num & 1<<i):
                    self.backtrack(nums,arr+[nums[i]],num | 1<<i,ind+1)
            return
        self.res.append(arr)