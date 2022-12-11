from heapq import heappop, heappush, heapify

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.arr = nums
        self.k = k

    def add(self, val: int) -> int:
        self.arr.append(val)
        heapify(self.arr)
        for _ in range(len(self.arr)-self.k):
            heappop(self.arr)
        ans = heappop(self.arr)
        self.arr.append(ans)
        return ans

        


        
        
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# 15 31