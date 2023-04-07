class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.rows = len(grid)
        self.cols = len(grid[0])
        
        for row in range(self.rows):
            for col in range(self.cols):
                if grid[row][col]:
                    return self.dfs(grid,row,col,4)
        
    def inbound(self,row, col):
        return (0 <= row < self.rows) and (0 <= col < self.cols)
    
    def dfs(self,grid,row,col,count):
        
        res = 0
        grid[row][col] = -1
        for row_change, col_change in self.directions:
            new_row = row + row_change
            new_col = col + col_change
            if self.inbound(new_row, new_col) and grid[new_row][new_col]:
                if grid[new_row][new_col] == 1:
                    res += self.dfs(grid, new_row, new_col,4)
                    count -= 1
                elif grid[new_row][new_col] == -1:
                    count -= 1
                
        return res + count
        