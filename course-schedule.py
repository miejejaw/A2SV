class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        dic = defaultdict(list)
        n = defaultdict(int)
        check = set()
        for num1 , num2 in prerequisites:
            dic[num2].append(num1)
            n[num1] += 1
            check.add(num1)
            
        visited = set()
        
        ans  = []
        for i in range(numCourses):
            if i not in visited and i not in check:
                queue = deque([i])
                visited.add(i)
                while queue:
                    temp = queue.popleft()
                    if n[temp] == 0:
                        ans.append(temp)
                    
                    for val in dic[temp]:
                        if n[val]==1  and val not in visited:
                            queue.append(val)
                            visited.add(val)
                        n[val] -= 1
                        
        return len(ans) == numCourses