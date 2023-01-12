class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        self.dic = defaultdict(list)
        self.labels = labels
        for node1,node2 in edges:
            self.dic[node1].append(node2)
            self.dic[node2].append(node1)
        
        self.ans = [0]*n
        self.trav(0)
        return self.ans
    
    def trav(self, key):
        res = defaultdict(int)
        letter = self.labels[key]
        res[letter] = 1
        
        while self.dic[key]:
            node = self.dic[key].pop()
            self.dic[node].remove(key)
            dic = self.trav(node)
            for k,val in dic.items():
                res[k] += val
        self.ans[key] = res[letter]
        return res
        