class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)-2
        res = [[0]*rows for i in range(rows)]
        for row in range(rows):
            for col in range(rows):
                res[row][col] = self.get_max(grid,row,col)
        return res
    
    def get_max(self, grid, row, col)-> int:
        max_num = 0
        for r in range(row,row+3):
            for c in range(col,col+3):
                max_num = max(max_num,grid[r][c])
        return max_num