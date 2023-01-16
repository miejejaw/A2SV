class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        for row in range(rows-2):
            for col in range(cols-2):
                count += self.checksum(grid[row][col], grid[row][col+1], grid[row][col+2],
                         grid[row+1][col], grid[row+1][col+1], grid[row+1][col+2],
                         grid[row+2][col], grid[row+2][col+1], grid[row+2][col+2])
        return count
    def checksum(self,a,b,c,d,e,f,g,h,i):
        temp = [1,2,3,4,5,6,7,8,9]
        nums = [a,b,c,d,e,f,g,h,i]
        nums.sort()
        if (temp==nums and (a+b+c == d+e+f == g+h+i == a+d+g ==b+e+h == c+f+i == a+e+i == c+e+g == 15)):
            return 1
        return 0

