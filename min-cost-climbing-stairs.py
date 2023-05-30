class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        self.length = len(cost)
        self.d = {}
        return min(self.dfs(cost,0),self.dfs(cost,1))
    
    def dfs(self, cost, ind):
        if ind < self.length:
            if ind in self.d: return self.d[ind]
            self.d[ind] = min(self.dfs(cost,ind+1),self.dfs(cost,ind+2))+cost[ind]
            return self.d[ind]
        return 0