class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        self.dic = defaultdict(list)
        self.s = s
        self.res = 0
        for ind,par in enumerate(parent):
            if ind:
                self.dic[par].append(ind)
        
        self.trav(0)
        return self.res
    def trav(self, parent):
        ans,res = [],0
        
        while self.dic[parent]:
            child = self.dic[parent].pop()
            count,child = self.trav(child)
            if self.s[parent] != child:
                res = max(res,count)
                ans.append(count)
        res += 1
        ans.sort(reverse=True)
        self.res = max(self.res,res,sum(ans[:2])+1)
        return [res,self.s[parent]]