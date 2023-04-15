class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        ans,seen = 0,set()
        self.length = len(isConnected)
        for row in range(self.length):
            if row not in seen:
                self.dfs(isConnected,row,seen)
                ans += 1
        return ans

    def dfs(self,isConnected,row,seen):
        if row not in seen:
            seen.add(row)
            for col,val in enumerate(isConnected):
                if col not in seen and isConnected[row][col]:
                    self.dfs(isConnected,col,seen)