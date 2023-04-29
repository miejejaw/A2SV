class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        self.rows,self.cols = len(mat),len(mat[0])
        queue = []
        for row in range(self.rows):
            for col in range(self.cols):
                if mat[row][col] == 0:
                    queue.append((row,col))
                    
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        res = [[0]*self.cols for _ in range(self.rows)]
        visited = set()
        distance = 1
        
        while queue:
            temp = []
            for x,y in queue:
                for row,col in directions:
                    row,col = row+x,col+y
                    if self.inbound(row,col) and (row,col) not in visited and mat[row][col] == 1:
                        temp.append((row,col))
                        res[row][col] = distance
                        visited.add((row,col))
            queue = temp
            distance += 1
        return res
    
    def inbound(self,row,col):
        return 0<=row<self.rows and 0<=col<self.cols