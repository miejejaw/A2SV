class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        for row in range(1,rows):
            for col in range(row):
                matrix[row][col],matrix[col][row] = matrix[col][row],matrix[row][col]
        for row in range(rows):
            matrix[row].reverse()
            
       