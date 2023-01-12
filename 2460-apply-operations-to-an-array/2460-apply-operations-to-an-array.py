class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        size = len(nums)
        for ind in range(1,size):
            if nums[ind]==nums[ind-1]:
                nums[ind] = 0
                nums[ind-1] *= 2
        beg = 0
        for end in range(size):
            if nums[end]:
                nums[end],nums[beg] = nums[beg],nums[end]
                beg += 1
        return nums