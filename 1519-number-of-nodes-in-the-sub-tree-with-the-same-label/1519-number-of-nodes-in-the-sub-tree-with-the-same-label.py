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
        res = [0]*26

        while self.dic[key]:
            node = self.dic[key].pop()
            self.dic[node].remove(key)
            temp = self.trav(node)
            for i,freq in enumerate(temp):
                res[i] += freq
                
        ind = ord(self.labels[key])-97
        res[ind] += 1
        self.ans[key] = res[ind]
        return res
        