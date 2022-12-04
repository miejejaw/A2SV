class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m,n = len(board),len(board[0])
        def trav(i,j):
            if i<0 or i==m or j<0 or j==n or board[i][j]!='O': return
            board[i][j] = 'A'
            trav(i+1,j)
            trav(i,j+1)
            trav(i-1,j)
            trav(i,j-1)
        for j,val in enumerate(board[0]):
            if val == 'O': trav(0,j) 
        for j,val in enumerate(board[m-1]):
            if val == 'O': trav(m-1,j)
        for j in range(1,m):
            trav(j,0)
        for j in range(1,m):
            trav(j,n-1)        
                
        for i,j in product(range(m),range(n)):
            if board[i][j] == 'O': board[i][j] = 'X'
            elif board[i][j] == 'A': board[i][j] = 'O'
        
        
# 10 00
        