class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:

        self.dp = {}
        return self.helper(poured,query_row,query_glass)[0]

    def helper(self,poured,row,col):
        
        if row:
            if (row,col) in self.dp: return self.dp[(row,col)]
            
            res = 0
            if col-1 >= 0:
                res = self.helper(poured,row-1,col-1)[1]
            if col < row:
                res += self.helper(poured,row-1,col)[1]

            self.dp[(row,col)] = (1,(res-1)/2) if res>=1 else (res,0)
            return self.dp[(row,col)]
        
        self.dp[(row,col)] =  (1,(poured-1)/2)if poured>=1 else (poured,0)
        return self.dp[(row,col)]