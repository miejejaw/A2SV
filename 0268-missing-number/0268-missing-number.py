class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = max(nums)
        arr_sum = (n * (n+1) // 2) - sum(nums)
        
        if not arr_sum and 0 in nums:
            return n+1
        else:
            return arr_sum
