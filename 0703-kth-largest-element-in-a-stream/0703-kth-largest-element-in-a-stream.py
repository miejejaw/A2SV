from heapq import heappop, heappush, heapify

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.arr = nums
        self.k = k
        heapify(self.arr)
        while len(self.arr) > k:
            heappop(self.arr)

    def add(self, val: int) -> int:
        heappush(self.arr,val)
        if len(self.arr) > self.k:
            heappop(self.arr)
            
        return self.arr[0]

        


        
        
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# 15 31