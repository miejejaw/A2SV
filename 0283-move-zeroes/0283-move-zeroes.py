class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0 
        size = len(nums)
        for index in range(size):
            if nums[index] != 0:
                nums[left],nums[index] = nums[index],nums[left]
                left += 1
        