class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        d = {}
        unionFind = UnionFind(d)
        for account in accounts:
            unionFind.union(account[1:])

        res = defaultdict(set)
        for k,v in d.items():
            v = unionFind.find(v)
            res[v].add(k)

        s = {}
        for account in accounts:
            name = account[0]
            for acc in account[1:]:
                s[acc] = name

        ans = []
        for k,v in res.items():
            acc = [s[k]] + sorted(list(v))
            ans.append(acc)
        return ans

class UnionFind:
    def __init__(self, d):
        self.root = d
    
    def find(self, a):
        if self.root[a] != a:
            self.root[a] = self.find(self.root[a]) 
        return self.root[a]

    def union(self, rows):
        a = rows[0]
        for b in rows:
            if b not in self.root:
                self.root[b] = b
            a = min(a,self.find(b))
        for b in rows:
            b = self.find(b)
            self.root[b] = a