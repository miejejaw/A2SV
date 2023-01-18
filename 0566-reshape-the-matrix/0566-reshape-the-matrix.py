class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        if rows*cols!=r*c or (r==rows and c==cols):
            return mat
        res = [[0]*c for _ in range(r)]
        matRow,matCol = 0,0
        for row in range(r):
            for col in range(c):
                res[row][col] = mat[matRow][matCol]
                matCol += 1
                if matCol==cols:
                    matCol = 0
                    matRow += 1
                
        
        return res