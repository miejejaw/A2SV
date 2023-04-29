class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        paths = defaultdict(list)
        for node1,node2 in edges:
            paths[node1].append(node2)
            paths[node2].append(node1)
        
        return self.dfs(paths,hasApple,0)
    
    def dfs(self, paths, hasApple, curr):
        
        total = 0
        while paths[curr]:
            node = paths[curr].pop()
            paths[node].remove(curr)
            total += self.dfs(paths,hasApple,node)
            
        if curr>0 and (hasApple[curr] or total>0):
            total += 2
            
        return total