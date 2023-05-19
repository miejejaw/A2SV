class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        length = len(stones)
        rows = defaultdict(list)
        cols = defaultdict(list)
        for i,point in enumerate(stones):
            rows[point[0]].append(i)
            cols[point[1]].append(i)
        
        unionFind = UnionFind(length)
        for _,row in rows.items():
            unionFind.union(row)
        for _,col in cols.items():
            unionFind.union(col)
        
        count = 0
        for i in range(length):
            if i != unionFind.find(i):
                count += 1
        return count
        
class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
    
    def find(self, a):
        if self.root[a] != a:
            self.root[a] = self.find(self.root[a]) 
        return self.root[a]

    def union(self, rows):
        a = 10000
        for b in rows:
            a = min(a,self.find(b))
        for b in rows:
            b = self.find(b)
            self.root[b] = a