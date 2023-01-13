class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        paths = set()
        row_len = len(matrix)
        col_len = len(matrix[0])
        
        for col in range(col_len-1):
            paths.add((0,col))
        for row in range(1,row_len-1):
            paths.add((row,0))
            
        for row,col in paths:
            row += 1
            col += 1
            while row_len>row and col_len>col:
                if matrix[row][col] != matrix[row-1][col-1]:
                    return False
                row += 1
                col += 1
        return True