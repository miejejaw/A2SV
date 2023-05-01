from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        self.rows,self.cols = len(maze),len(maze[0])
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        queue = deque([(entrance[0],entrance[1],0)])
        seen = set((entrance[0],entrance[1]))

        while queue:
            x,y,d = queue.popleft()
           
            if [x,y] != entrance and (self.rows==x+1 or x==0 or self.cols==y+1 or y==0):
                return d
            for row,col in direction:
                row,col = row+x,col+y
                if self.inbound(row,col) and (row,col) not in seen and maze[row][col]==".":
                    seen.add((row,col))
                    queue.append((row,col,d+1))
                    
        return -1
    
    def inbound(self,row,col):
        return 0<=row<self.rows and 0<=col<self.cols