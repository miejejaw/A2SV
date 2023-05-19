class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        unionFind = UnionFind(len(edges))
        ans = []
        for a, b in edges:
            if unionFind.union(a,b):
                ans = [a,b]
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
        self.root[b] = a

        return a == b