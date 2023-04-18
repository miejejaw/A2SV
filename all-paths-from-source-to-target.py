class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.res = []
        self.dfs(graph,len(graph)-1,0,[0])
        return self.res
    
    def dfs(self, graph, n, ind, path):
        
        if ind != n:
            for node in graph[ind]:
                self.dfs(graph,n,node,path+[node])
            return 
    
        self.res.append(path)