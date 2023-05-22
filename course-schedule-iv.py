class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        graph = defaultdict(list)
        seen = set()
        for c1,c2 in prerequisites:
            graph[c1].append(c2)
            seen.add(c2)
        isReachable = [[False]*numCourses for _ in range(numCourses)]
        self.r = {}
        for course in range(numCourses):
            if course not in seen:
                self.dfs(graph,isReachable,course)

        length = len(queries)
        ans = [False]*length
        for ind in range(length):
            ans[ind] = isReachable[queries[ind][0]][queries[ind][1]]
        return ans

    def dfs(self, graph, isReachable, pre):
        
        temp = []
        for course in graph[pre]:
            if course in self.r:
                temp += self.r[course]+[course]
            else:
                temp += self.dfs(graph, isReachable,course)
        
        temp = list(set(temp))
        for c in temp:
            isReachable[pre][c] = True
        self.r[pre] = temp
        return temp+[pre]