from heapq import heapify,heappop
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        heap = [(-freq,word) for word,freq in Counter(words).items()]
        heapify(heap)
        ans = [heappop(heap)[1] for _ in range(k)]
        return ans