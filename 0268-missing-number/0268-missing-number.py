class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)
        arr_dif = (n * (n+1) // 2) - sum(nums)
        
        if not arr_dif and 0 in nums:
            return n+1
        else:
            return arr_dif
