from queue import PriorityQueue
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        q,ans = PriorityQueue(),[]
        for st,freq in Counter(words).items():
            q.put((-freq,st))
        for _ in range(k):
            ans.append(q.get()[1])
  
        return ans

        