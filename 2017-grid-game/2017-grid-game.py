class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        if len(grid[0]) == 1:
            return 0
        grid[0] = list(reversed(list(accumulate(grid[0][::-1]))))
        grid[1] = list(accumulate(grid[1]))
        ans = [grid[0][1],grid[1][-2]]
        for ind in range(1,len(grid[0])-1):
            ans.append(max(grid[0][ind+1],grid[1][ind-1]))
            
        return min(ans)
            
    