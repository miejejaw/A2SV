class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        self.dp = {}
        self.rows = len(triangle)
        return self.helper(triangle,0,0)
    
    def helper(self,triangle,row,col):
        if row < self.rows:
            if (row,col) in self.dp: return self.dp[(row,col)]
            res = self.helper(triangle,row+1,col)
            res = min(res,self.helper(triangle,row+1,col+1))
            self.dp[(row,col)] = res+triangle[row][col]

            return self.dp[(row,col)] 
        return 0