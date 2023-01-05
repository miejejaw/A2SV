class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        arr = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
        ans = []
        queens = set(map(tuple,queens))
        for dx,dy in arr:
            x = king[0]+dx
            y = king[1]+dy
            while 0<=x<8 and 0<=y<8:
                if (x,y) in queens:
                    ans.append([x,y])
                    break
                x += dx
                y += dy
        return ans