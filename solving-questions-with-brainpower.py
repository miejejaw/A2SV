class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:

        self.length = len(questions)
        self.dp = {}
        ans = 0
        for ind in range(self.length):
            ans = max(ans,self.helper(questions,ind))
        return ans

    def helper(self, questions, ind):
        if ind < self.length:
            if ind in self.dp: return self.dp[ind]
            res = 0
            temp = ind+questions[ind][1]+1
            for i in range(temp,self.length):
                res = max(res,self.helper(questions,i))
            self.dp[ind] = res+questions[ind][0]
            return self.dp[ind]
        return 0