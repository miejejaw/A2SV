class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        col_set = set()
        row_set = set()
        rows,cols = len(matrix),len(matrix[0])
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col]==0:
                    col_set.add(col)
                    row_set.add(row)
        for row in range(rows):
            for col in range(cols):
                if row in row_set or col in col_set:
                    matrix[row][col] = 0
 
        
        