class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        connected = set()
        nums = [[i,0] for i in range(n)]
        for city1,city2 in roads:
            nums[city1][1] += 1
            nums[city2][1] += 1
            connected.add((city1,city2))
        
        ans = 0
        for i in range(n):
            for j in range(i+1,n):
                total = nums[j][1] + nums[i][1]
                if (nums[j][0],nums[i][0]) in connected or (nums[i][0],nums[j][0]) in connected:
                    total -= 1
                ans = max(ans,total)
        
        return ans