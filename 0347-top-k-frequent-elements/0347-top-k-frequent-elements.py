class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        cnt = Counter(nums)
        heap = [[+freq, num] for num, freq in cnt.items()]
        largest = heapq.nlargest(k, heap)
        ans = [key for value, key in largest]
        return ans