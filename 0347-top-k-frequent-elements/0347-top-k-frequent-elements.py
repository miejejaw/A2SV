class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            dic[i] = dic.get(i,0)+1
        heap = [(value, key) for key,value in dic.items()]
        largest = heapq.nlargest(k, heap)
        ans = [key for value, key in largest]
        return ans