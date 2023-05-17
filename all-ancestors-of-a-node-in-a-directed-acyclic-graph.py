class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        graph = defaultdict(list)
        seen = set()
        for from_node, to_node in edges:
            graph[to_node].append(from_node)
            seen.add(from_node)
        self.ans = [[] for _ in range(n)]
            
        for node in range(n):
            if node not in seen:
                self.dfs(graph,node)   
                
        return self.ans
    
    def dfs(self, graph, curr):
        
        res = set()
        for node in graph[curr]:
            temp = self.ans[node]+[node] 
            if not self.ans[node]:
                temp = self.dfs(graph,node)  
            res.update(temp)
            
        self.ans[curr] = sorted(list(res))
        return self.ans[curr]+[curr]