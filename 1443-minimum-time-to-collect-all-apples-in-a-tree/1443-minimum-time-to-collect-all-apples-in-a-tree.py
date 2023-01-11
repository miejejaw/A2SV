class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        self.dic = defaultdict(list)
        for v1,v2 in edges:
            self.dic[v1].append(v2)
            self.dic[v2].append(v1)
        size = len(hasApple) 
        hasApple[0] = False
        ans = self.trav(hasApple,0)*2 - 2
        if ans<0: 
            return 0
        return ans
    
    def trav(self, hasApple, key):
        ans = 0        
        while self.dic[key]:
            col = self.dic[key].pop()
            self.dic[col].remove(key)
            ans += self.trav(hasApple,col)
            
        if ans:
            ans += 1
        elif hasApple[key]:
            ans = 1
        return ans       
                
                
