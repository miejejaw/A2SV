class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        if n == 1: return [0]
        if n == 2: return [0,1]
        graph = defaultdict(list)
        indegree = [0]*n
        for node1,node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
            indegree[node1] += 1
            indegree[node2] += 1

        queue = deque()
        visited = set()
        for node in range(n):
            if indegree[node] == 1:
                queue.append(node)
                visited.add(node)

        length = len(queue)
        while queue:
            for _ in range(length):
                curr = queue.popleft()
                for node in graph[curr]:
                    indegree[node] -= 1
                    if indegree[node] == 1 and node not in visited:
                        queue.append(node)
                        visited.add(node)

            length = len(queue)
            if length <= 2 and n == len(visited): break

        return list(queue)