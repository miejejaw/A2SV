class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]: return -1
        elif len(grid) == 1: return 1
        self.length = len(grid)
        self.count = 1
        self.directions = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]
        res = self.bfs(grid,set(),set({(0,0)}))
        return self.count if res else -1
    
    def inbound(self,row,col):
        return 0<=row<self.length and 0<=col<self.length
    
    def bfs(self, grid, visited, paths):
        
        nextPaths = set()
        for path in paths:
            visited.add(path)
            for row,col in self.directions:
                row += path[0]
                col += path[1]
                if (3,2) == path:
                    print(row,col)
                if self.inbound(row,col) and (row,col) not in visited and grid[row][col] == 0:
                    nextPaths.add((row,col))
        res = False               
        if nextPaths:
            self.count += 1
            if (self.length-1,self.length-1) in nextPaths:
                return True
            res = self.bfs(grid,visited,nextPaths)

        return res