class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        cites = defaultdict(set)
        nums = [[0,i] for i in range(n)]
        for city1,city2 in roads:
            cites[city1].add(city2)
            cites[city2].add(city1)
            nums[city1][0] += 1
            nums[city2][0] += 1
        
        ans = 0
        for i in range(n):
            for j in range(i+1,n):
                total = nums[j][0] + nums[i][0]
                if nums[j][1] in cites[nums[i][1]]:
                    total -= 1
                ans = max(ans,total)
        
        return ans