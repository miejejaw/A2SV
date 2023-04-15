class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.color = color
        self.image_color = image[sr][sc]
        self.row_len = len(image)
        self.col_len = len(image[0])
        self.image = image
        self.arr = [(1,0),(-1,0),(0,1),(0,-1)]
        self.trav(sr,sc)
        return self.image
    
    def trav (self, row, col):
        if row<0 or row==self.row_len or col<0 or col==self.col_len:
            return
        if self.image[row][col]!=self.image_color or self.image[row][col]==self.color:
            return 
        self.image[row][col] = self.color
        for r,c in self.arr:
            self.trav(row+r,col+c)