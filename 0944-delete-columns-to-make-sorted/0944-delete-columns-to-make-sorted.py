class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        col_len = len(strs[0])
        row_len = len(strs)
        res = 0 
        for ind in range(col_len):
            for w in range(1,row_len):
                if strs[w-1][ind] > strs[w][ind]:
                    res += 1
                    break
                    
        return res