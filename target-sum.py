class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        self.d = defaultdict(int)
        self.target = target
        self.length = len(nums)
        return self.dfs(nums,0,0)

    def dfs(self,nums,ind,total):
        if ind < self.length:
            if (total,ind) in self.d: 
                return self.d[(total,ind)]
    
            res = self.dfs(nums,ind+1,total+nums[ind])
            res += self.dfs(nums,ind+1,total-nums[ind])
            self.d[(total,ind)] = res
            return self.d[(total,ind)]
        return self.target == total