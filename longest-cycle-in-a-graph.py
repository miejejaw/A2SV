class Solution:
    def longestCycle(self, edges: List[int]) -> int:

        length,self.seen = len(edges),set()

        ans = -1
        for node in range(length):
            if node not in self.seen:
                ans = max(ans,self.dfs(edges,node,set())[1])
                                                                                
        return ans

    def dfs(self, graph, curr, visited):
        if curr != -1 and curr not in self.seen:
            visited.add(curr)
            self.seen.add(curr)
            node,count = self.dfs(graph,graph[curr],visited)
            if curr == node: return -1,count
            if node != -1: count += 1
            return node,count
            
        if curr in visited: return curr,1
        return -1,-1