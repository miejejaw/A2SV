import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-num for num in stones]+[0]
        length = len(stones)
        heapq.heapify(stones)
        while length > 1:
            num1,num2 = heapq.heappop(stones),heapq.heappop(stones)
            heapq.heappush(stones,num1-num2)
            length -= 1
        
        return -stones[0]