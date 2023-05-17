class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        length,ans,visited = len(graph),set(),set()
        
        for ind in range(length):
            if ind not in visited:
                self.dfs(graph,visited,ind,ans)
               
        return sorted(list(ans))    
              
    def dfs(self, graph, visited, curr, ans):
        
        if curr not in visited:
            
            visited.add(curr)
            res = -1

            for node in graph[curr]:
                res = max(res,self.dfs(graph,visited,node,ans))

            if res == -1:
                ans.add(curr) 
            return res
        
        return -1 if curr in ans else curr