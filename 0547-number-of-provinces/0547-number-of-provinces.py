class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def helper(i: int)-> int:            
            for j in range(len(isConnected)):           
                if isConnected[i][j]==1:
                    isConnected[i][j] = 2
                    isConnected[j][i] = 2
                    helper(j)
            return 1
        ans = 0
        for i in range(len(isConnected)):           
            if isConnected[i][i]==1:
                isConnected[i][i]=2
                ans += helper(i)
        return ans
        
        
#13 18
        