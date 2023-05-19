class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        length = len(s1)
        unionFind = UnionFind(26)
        for ind in range(length):
            unionFind.union(ord(s1[ind])-97,ord(s2[ind])-97)

        ans = ""
        for a in baseStr:
            ans += chr(unionFind.find(ord(a)-97)+97)
        return ans

class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        
    def find(self, a):
        if self.root[a] != a:
            self.root[a] = self.find(self.root[a]) 
        return self.root[a]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a > b:
            a,b = b,a
        self.root[b] = a