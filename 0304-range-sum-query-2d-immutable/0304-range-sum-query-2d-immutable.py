class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.matrix = [[0]*(cols+1) for _ in range(rows+1)]
        for row in range(rows):
            for col in range(cols):
                self.matrix[row+1][col+1] = matrix[row][col] + self.matrix[row][col+1] + self.matrix[row+1][col] - self.matrix[row][col]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = self.matrix[row2+1][col2+1] - self.matrix[row2+1][col1] - self.matrix[row1][col2+1] + self.matrix[row1][col1] 
        return ans