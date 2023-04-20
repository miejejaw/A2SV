class Solution:
    def solve(self, board: List[List[str]]) -> None:
        onborder = set()
        self.rows,self.cols = len(board),len(board[0])
        self.directions = [(0,-1),(-1,0),(0,1),(1,0)]
        for col in range(self.cols):
            if (0,col) not in onborder and board[0][col] == "O":
                self.dfs(board,onborder,0,col)
            if (self.rows-1,col) not in onborder and board[self.rows-1][col] == "O":
                self.dfs(board,onborder,self.rows-1,col)
                
        for row in range(self.rows):
            if (row,0) not in onborder and board[row][0] == "O":
                self.dfs(board,onborder,row,0)
            if (row,self.cols-1) not in onborder and board[row][self.cols-1] == "O":
                self.dfs(board,onborder,row,self.cols-1)
                
        
        for row in range(1,self.rows):
            for col in range(1,self.cols):
                if (row,col) not in onborder and board[row][col] == "O":
                    board[row][col] = "X"
        
        
        
    def dfs(self, board, onborder, row, col):
        onborder.add((row,col))
        for x,y in self.directions:
            x += row
            y += col
            if self.inbound(x,y) and (x,y) not in onborder and board[x][y]=="O":
                self.dfs(board,onborder,x,y)
                
    def inbound(self, row, col):
        return 0<=row<self.rows and 0<=col<self.cols