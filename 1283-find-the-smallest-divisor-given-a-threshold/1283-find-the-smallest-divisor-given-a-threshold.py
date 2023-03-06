class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        
        while left < right:
            mid = left + (right-left)//2
            if self.helper(nums,mid,threshold):
                right = mid
            else:
                left = mid + 1      
        return left
    
    def helper(self, nums, div, threshold):
        total = 0
        for num in nums:
            total += ceil(num/div)
        return total <= threshold
    