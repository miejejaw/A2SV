class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_len,col_len,row = len(matrix)-1,len(matrix[0]),0
        for i in range(row_len,-1,-1):
            if matrix[i][0] <= target:
                row = i
                break
        for i in range(col_len):
            if matrix[row][i] == target:
                return True
            
        return False