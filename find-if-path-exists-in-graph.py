class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        self.ans = False
        adjList = defaultdict(list)
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
            
        self.dfs(adjList,source,destination)
        return self.ans
    
    def dfs(self,adjList,vertex,destination):
        if not self.ans:
            if vertex == destination:
                self.ans = True
                return
            while adjList[vertex]:
                vex = adjList[vertex].pop()
                self.dfs(adjList,vex,destination)