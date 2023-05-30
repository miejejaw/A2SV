class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        coins.sort(reverse=True)
        self.d = defaultdict()
        for coin in coins:
            self.d[coin] = 1
        ans = self.dfs(coins,amount)
        return ans if ans<float("inf") else -1
    
    def dfs(self, coins,amount):
        if amount in self.d: return self.d[amount]
        if amount <= 0: return float("inf")
        res = float("inf")
        for coin in coins:
            res = min(res,self.dfs(coins,amount-coin))

        self.d[amount] = res+1
        return self.d[amount]