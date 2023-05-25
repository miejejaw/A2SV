class Solution:
    def minDifference(self, nums: List[int]) -> int:

        length = len(nums)
        if length < 5: return 0
        nums.sort()
        res = float("inf")
        
        j = length-1
        for i in range(3,-1,-1):
            res = min(res,nums[j]-nums[i])
            j -= 1
            
        return res