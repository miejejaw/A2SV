class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        arr = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
        ans = []
        for x,y in arr:
            temp = [king[0]+x,king[1]+y]
            while 0<=temp[0]<8 and 0<=temp[1]<8:
                if temp in queens:
                    ans.append(temp)
                    break
                temp[0] += x
                temp[1] += y
        return ans