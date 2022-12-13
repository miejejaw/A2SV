from queue import PriorityQueue
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        q = PriorityQueue()
        for row in matrix:
            for num in row:
                q.put(-num)
                if q.qsize()>k and num == -q.get():
                    break
        return -q.get()
        
        