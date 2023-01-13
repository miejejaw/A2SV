class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        dic = {}
        row_len = len(matrix)
        col_len = len(matrix[0])
        
        for col,num in enumerate(matrix[0]):
            dic[(0,col)] = num
        for row in range(1,row_len):
            dic[(row,0)] = matrix[row][0]
            
        for row in range(row_len):
            for col in range(col_len):
                temp = min(row,col)
                if matrix[row][col] != dic[(row-temp,col-temp)]:
                    return False
        return True