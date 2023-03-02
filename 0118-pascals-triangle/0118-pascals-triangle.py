class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        self.pascal = [[1]]
        self.helper(numRows-1)
        return self.pascal
    
    def helper(self, row):
        if row == 0:
            return [1] 
        res = self.helper(row-1)
        
        ans = [1]*(row+1)
        for ind in range(1,row):
            ans[ind] = res[ind-1] + res[ind]
        self.pascal.append(ans)
        return ans
              