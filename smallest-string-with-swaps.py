class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        length = len(s)
        unionFind = UnionFind(length)
        for a, b in pairs:
            unionFind.union(a,b)

        res = defaultdict(list)
        for ind in range(length):
            a = unionFind.find(ind)
            res[a].append(ind)

        s = list(s)
        for _,arr in res.items():
            arr.sort()
            temp = []
            for ind in arr:
                temp.append(s[ind])
            temp.sort()
            i=0
            for ind in arr:
                s[ind] = temp[i]
                i += 1

        return "".join(s)

   
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