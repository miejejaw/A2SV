class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left = 0 
        size = len(nums)
        for index in range(size):
            if nums[index] %2 == 0:
                nums[left],nums[index] = nums[index],nums[left]
                left += 1
        return nums