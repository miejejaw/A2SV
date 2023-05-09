from queue import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        if "0000" == target: return 0
        if "0000" in deadends: return -1
        
        deadends = list(map(list,deadends))
        deadends = [tuple(map(int,deadend)) for deadend in deadends]
        deadends = set({*deadends})
        visited = set()
        queue = deque([((0,0,0,0),0)])
        target = tuple(map(int,target))
        
        while queue:
            lock,rotateCount = queue.popleft()
            rotateCount += 1
            for ind in range(4):
                down = list(lock[:])
                up = list(lock[:])
                up[ind] += 1
                if up[ind] == 10:
                    up[ind] = 0
                down[ind] -= 1
                if down[ind] == -1:
                    down[ind] = 9
                down,up = tuple(down),tuple(up)

                if down == target or up == target:
                    return rotateCount
                if down not in deadends and down not in visited:
                    queue.append((down,rotateCount))
                    visited.add(down)
                if up not in deadends and up not in visited:
                    queue.append((up,rotateCount))
                    visited.add(up)
                
        return -1