class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        length = len(parent)
        paths = defaultdict(list)
        for node in range(1,length):
            paths[parent[node]].append(node)
        self.ans = 0
        self.dfs(paths,s,0)[1]
        return self.ans 
    
    def dfs(self, paths, s, curr):
        one = 0
        two = 0
        for node in paths[curr]:
            res = self.dfs(paths,s,node)
            if res[0] != s[curr]:
                if res[1] > one:
                    two = one
                    one = res[1]
                elif res[1] > two:
                    two = res[1]
        self.ans = max(self.ans,one+two+1)
        return [s[curr],one+1]