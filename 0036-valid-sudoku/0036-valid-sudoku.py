class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #check each row
        for row in board:
            cells = set()
            for cell in row:
                if cell!="." and cell in cells:
                    return False
                cells.add(cell)
        
        #check each col
        for col in range(9):
            cells = set()
            for row in range(9):
                if board[row][col]!="." and board[row][col] in cells:
                    return False
                cells.add(board[row][col])
        
        #check each 3X3 matrixs
        for rows in range(0,9,3):
            for cols in range(0,9,3):
                cells = set()
                for row in range(rows,rows+3):
                    for col in range(cols,cols+3):
                        if board[row][col]!="." and board[row][col] in cells:
                            return False
                        cells.add(board[row][col])
        
        return True
                
            