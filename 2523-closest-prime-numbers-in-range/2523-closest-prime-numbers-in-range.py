class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
        visited = [1]*(right+1)
        visited[1] = 0
        
        for i in range(2,right+1):
            if visited[i]:
                for j in range(i*i,right+1,i):
                    visited[j] = 0
                    
        res = [-1,-1]
        prev = 0
        for ind in range(left,right+1):
            if visited[ind]:
                if prev > 0 and res[0] == -1:
                    res[0] = prev
                    res[1] = ind
                elif ind - prev < res[1]-res[0]:
                    res[0] = prev
                    res[1] = ind
                    
                prev = ind
                
        return res
                    