class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        return self.helper(rowIndex)
    
    def helper(self, row):
        if row == 0:
            return [1]
        res = self.helper(row-1)
        ans = [1]*(row+1)
        for ind in range(1,row):
            ans[ind] = res[ind-1] + res[ind]
        return ans
            
        