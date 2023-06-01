class Solution:
    def rob(self, nums: List[int]) -> int:
        
        length = len(nums)
        ans = nums[-1]
        self.d = {}
        ans =  max(self.dp(nums,0,length-1),ans)
        self.d = {}
        for ind in range(1,length):
            ans =  max(self.dp(nums,ind,length),ans)
        
        return ans

    def dp(self, nums, ind,length):
        if ind < length:
            if ind in self.d: return self.d[ind]
            self.d[ind] = max(self.dp(nums,ind+2,length),self.dp(nums,ind+3,length))
            self.d[ind] += nums[ind]
            return self.d[ind]
        return 0