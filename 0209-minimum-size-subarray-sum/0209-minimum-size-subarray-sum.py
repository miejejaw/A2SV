class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        beg = total = 0
        size = len(nums)
        res = size+1 
        
        for end in range(size):
            total += nums[end]
            while total >= target:
                res = min(res,end-beg+1)
                total -= nums[beg]
                beg += 1
            
        return  res if res < size+1 else 0
    