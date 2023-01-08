class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        self.row_len,self.col_len = len(grid2),len(grid2[0])
        self.arr = [(1,0),(-1,0),(0,1),(0,-1)]
        count = 0
        for row in range(self.row_len):            
            for col in range(self.col_len):                
                if grid2[row][col]:
                    count += self.trav(grid1,grid2,row,col)
        return count
    
    def trav (self, grid1, grid2, row, col):
        if row<0 or row==self.row_len or col<0 or col==self.col_len or grid2[row][col]==0:
            return True
        res  = True
                
        grid2[row][col] = 0
        for r,c in self.arr:
            res = self.trav(grid1,grid2,row+r,col+c) and res
        return res and grid1[row][col]