from queue import PriorityQueue
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q = PriorityQueue()
        q.put(0)
        for i in stones:
            q.put(-i)
        while q.qsize()>1:
            x = q.get()
            y = q.get()
            if y-x != 0:
                q.put(x-y)
        return -q.get()
        