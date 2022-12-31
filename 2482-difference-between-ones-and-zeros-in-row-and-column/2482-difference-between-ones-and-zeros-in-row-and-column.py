
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        
        one_row = []
        for row in grid:
            one_row.append(sum(row))
        one_col = []
        for row in zip(*grid):
            one_col.append(sum(row))
            
        row,col = len(grid),len(grid[0])
        for i in range(row):
            for j in range(col):
                grid[i][j] = 2*one_col[j] + 2*one_row[i] - row - col
        return grid