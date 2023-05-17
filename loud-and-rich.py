class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        
        graph = defaultdict(list)
        seen = set()
        for from_node, to_node in richer:
            graph[to_node].append(from_node)
            seen.add(from_node)
        
        length = len(quiet)
        self.ans = [600]*length
            
        for node in range(length):
            if node not in seen:
                self.dfs(graph,quiet,node)   
                
        return self.ans
    
    def dfs(self, graph, quiet, curr):
        
        res = [quiet[curr],curr]
        
        for node in graph[curr]:
            temp = 0
            if self.ans[node] == 600:
                temp = self.dfs(graph,quiet,node)
            else:
                temp = [quiet[self.ans[node]],self.ans[node]]
            if temp[0] < res[0]:
                res = temp
        
        self.ans[curr] = res[1]       
        return res