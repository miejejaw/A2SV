class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        unionFind = UnionFind(n)
        for a, b, _ in roads:
            unionFind.union(a,b)
            
        ans = 100000
        temp = unionFind.find(n)
        for a,b,d in roads:
            if temp == unionFind.find(a):
                ans = min(ans,d)
        return ans
    
    
class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n+1)]
        
    def find(self, a):
        if self.root[a] != a:
            self.root[a] = self.find(self.root[a]) 
        return self.root[a]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        self.root[a] = b