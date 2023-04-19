class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        length = len(bombs)
        bombsDetonate = self.getDetonatedBombs(bombs,length)
        
        ans = 0
        for bomb in range(length):
            seen = set()
            self.dfs(bombsDetonate,bomb,seen) 
            ans = max(ans,len(seen))
        return ans
     
    def dfs(self, bombsDetonate, bomb, seen):

        seen.add(bomb)
        for detonated in bombsDetonate[bomb]:
            if detonated not in seen:
                self.dfs(bombsDetonate,detonated,seen) 
            
    def getDetonatedBombs(self,bombs,length):
        bombsDetonate = [0]*length
        for ind in range(length):
            temp = []
            for i in range(length):
                if ind != i:
                    x = pow(bombs[ind][0]-bombs[i][0],2)
                    y = pow(bombs[ind][1]-bombs[i][1],2)
                    gap = math.sqrt(x+y)
                    if gap <= bombs[ind][2]:
                        temp.append(i)
            bombsDetonate[ind] = temp
        return bombsDetonate