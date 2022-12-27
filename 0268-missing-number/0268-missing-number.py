class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)
        arr_dif = (n * (n+1) // 2) - sum(nums)
               
        return arr_dif
