from heapq import heapify,heappush,heappop
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        piles = [-num for num in piles]
        heapify(piles)
        for _ in range(k):
            num = heappop(piles)
            heappush(piles,num//2)
            
        return -sum(piles)