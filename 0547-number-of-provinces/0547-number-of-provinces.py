class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ans = 0
        def helper(i): 
            while 1 in isConnected[i]:           
                j = isConnected[i].index(1)
                isConnected[i][j] = 0
                isConnected[j][i] = 0
                helper(j)
        for i in range(len(isConnected)):           
            if isConnected[i][i]==1:
                isConnected[i][i] = 0
                helper(i)
                ans += 1
        return ans
        
        
#13 18
        