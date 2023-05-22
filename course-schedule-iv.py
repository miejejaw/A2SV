class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        graph = defaultdict(list)
        seen = set()
        for c1,c2 in prerequisites:
            graph[c1].append(c2)
            seen.add(c2)
            
        isReachable = {}
        for course in range(numCourses):
            if course not in seen:
                self.dfs(graph,isReachable,course)

        length = len(queries)
        ans = [False]*length
        for ind in range(length):
            if queries[ind][1] in isReachable[queries[ind][0]]:
                ans[ind] = True
        return ans

    def dfs(self, graph, isReachable, pre):
        
        temp = set()
        for course in graph[pre]:
            if course in isReachable:
                temp.update(isReachable[course])
                temp.add(course)
            else:
                temp.update(self.dfs(graph, isReachable,course))
        
        isReachable[pre] = temp
        temp.add(pre)
        return temp