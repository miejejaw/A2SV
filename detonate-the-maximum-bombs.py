class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        length = len(bombs)
        bombsDetonate = self.getDetonatedBombs(bombs,length)
        
        self.visited = set()
        self.ans = 0
        for bomb in range(length):
            self.dfs(bombsDetonate,bomb,set({bomb})) 
            self.visited.clear()
        return self.ans
     
    def dfs(self, bombsDetonate, bomb, seen):

        self.ans = max(self.ans,len(seen))
        if bombsDetonate[bomb]:
            self.visited.add(bomb)
            seen.update(bombsDetonate[bomb])
            for detonated in bombsDetonate[bomb]:
                if detonated not in self.visited:
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