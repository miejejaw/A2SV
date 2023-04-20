class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board
        
        self.rows,self.cols = len(board),len(board[0])
        self.directions = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
        self.dfs(board,set(),click[0],click[1])
        return board
    
    def inbound(self,row,col):
        return 0<=row<self.rows and 0<=col<self.cols
    
    def dfs(self, board, seen, row, col):
        
        seen.add((row,col))
        res = self.check(row,col,board)
        if res > 0:
            board[row][col] = str(res)
        else:
            board[row][col] = "B"
            
        for x,y in self.directions:
            x += row
            y += col
            if self.inbound(x,y) and (x,y) not in seen:
                if board[x][y] == "E" and board[row][col] == "B":
                    self.dfs(board,seen,x,y)
                 
            
    def check(self, row, col, board):
        total = 0
        for x,y in self.directions:
            x += row
            y += col
            if self.inbound(x,y) and board[x][y] == "M":
                total += 1
                
        return total