class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:

        graph = defaultdict(list)
        seen = set()
        for n1,n2 in adjacentPairs:
            if n1 in seen and n1 in graph:
                seen.remove(n1)
            elif n1 not in graph:
                seen.add(n1)
            
            if n2 in seen and n2 in graph:
                seen.remove(n2)
            elif n2 not in graph:
                seen.add(n2)

            graph[n1].append(n2)
            graph[n2].append(n1)

        ans = []
        visited = set()
        for node in seen:
            if node not in visited:
                ans.append(node)
                self.dfs(graph,node,visited,ans)
        
        return ans

    def dfs(self, graph, curr, visited,ans):
        visited.add(curr)
        for node in graph[curr]:
            if node not in visited:
                ans.append(node)
                self.dfs(graph,node,visited,ans)