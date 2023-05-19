class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        unionFind = UnionFind(n)
        for a, b in edges:
            unionFind.union(a,b)

        return unionFind.find(source) == unionFind.find(destination)    
    
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