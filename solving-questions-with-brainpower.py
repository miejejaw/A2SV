class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:

        self.length = len(questions)
        self.dp,ans = {},0
        for ind in range(self.length):
            ans = max(ans,self.helper(questions,ind))
        return ans

    def helper(self, nums, ind):
        if ind < self.length:
            if ind in self.dp: return self.dp[ind]
            res = self.helper(nums,ind+nums[ind][1]+1)+nums[ind][0]
            res = max(res,self.helper(nums,ind+1))
            self.dp[ind] = res
            return self.dp[ind]
        return 0