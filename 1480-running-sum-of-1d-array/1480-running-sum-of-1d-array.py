class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        size = len(nums)
        for ind in range(1,size):
            nums[ind] += nums[ind-1]
        return nums
            