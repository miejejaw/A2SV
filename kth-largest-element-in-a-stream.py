from heapq import heappop, heappush, heapify

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.arr = nums
        self.k = k
        heapify(self.arr)
        self.length = len(nums)
        while k < self.length:
            heappop(self.arr)
            self.length -= 1

    def add(self, val: int) -> int:
        heappush(self.arr,val)
        self.length += 1
        if self.k < self.length:
            heappop(self.arr)
            self.length -= 1
            
        return self.arr[0]