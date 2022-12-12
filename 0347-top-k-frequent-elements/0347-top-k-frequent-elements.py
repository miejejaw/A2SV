from queue import PriorityQueue
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        q,ans = PriorityQueue(),[]
        for num,freq in Counter(nums).items():
            q.put((freq,num))
            if q.qsize()>k: q.get()
                      
        while not q.empty():
            ans.append(q.get()[1])
        return ans