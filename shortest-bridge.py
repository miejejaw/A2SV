class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        self.length = len(grid)
        self.direction = [(1,0),(0,1),(-1,0),(0,-1)]
        queue = deque()
        visited = set()
        for row in range(self.length):
            for col in range(self.length):
                if grid[row][col] == 1:
                    self.dfs(grid,queue,visited,row,col)
                    return self.bfs(grid,queue,visited)

    def bfs(self, grid, queue,visited): 
        
        while queue:
            row,col,p = queue.popleft()
            p += 1
            for x,y in self.direction:
                x,y = x+row,y+col
                if self.inbound(x,y) and (x,y) not in visited:
                    if grid[x][y] == 1:
                        return p-1
                    queue.append((x,y,p))
                    visited.add((x,y))
    
    def dfs(self, grid, queue, seen, row, col):
        
        queue.append((row,col,0))
        seen.add((row,col))
        for x,y in self.direction:
            x,y = x+row,y+col
            if self.inbound(x,y) and (x,y) not in seen and grid[x][y]:
                self.dfs(grid,queue,seen,x,y)
        
    def inbound(self, row, col):
        return 0<=row<self.length and 0<=col<self.length