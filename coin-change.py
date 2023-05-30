class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.d = {}
        ans = self.dfs(coins,amount)
        return ans if ans<float("inf") else -1
    
    def dfs(self, coins,amount):
        if amount in self.d: return self.d[amount]
        if amount == 0: return 0
        res = float("inf")
        for coin in coins:
            if amount-coin >= 0:
                res = min(res,self.dfs(coins,amount-coin))
        self.d[amount] = res+1
        return self.d[amount]