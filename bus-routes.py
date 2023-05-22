class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target: return 0
        routes = list(map(set,routes))
        graph = defaultdict(list)
        length = len(routes)
        for ind in range(length):
            if source in routes[ind] and target in routes[ind]:
                return 1
            for i in range(ind+1,length):
                if routes[ind] & routes[i]:
                    graph[ind].append(i)
                    graph[i].append(ind)
        s = -1
        for ind,route in enumerate(routes):
            if source in route:
                s = ind
        t = -1
        for ind,route in enumerate(routes):
            if target in route:
                t = ind

        if t!=-1 and s!=-1:
            visited = set({s})
            queue = deque([(s,1)])
            while queue:
                curr,bus = queue.popleft()
                if curr == t: return bus
                bus += 1
                for node in graph[curr]:
                    if node not in visited:
                        queue.append((node,bus))
                        visited.add(node)
        return -1