class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        self.d = {0:1}
        ans = self.dfs(nums,target)
        return ans 
    
    def dfs(self, nums,target):
        if target in self.d: return self.d[target]
        res = 0
        for num in nums:
            if target-num >= 0:
                res += self.dfs(nums,target-num)
        self.d[target] = res
        return self.d[target]