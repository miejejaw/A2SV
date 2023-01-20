class Solution:
    def sortColors(self, nums: List[int]) -> None:
        size = len(nums)
        for ind in range(1,size): 
            left = ind
            temp = nums[ind]
            while left>0 and temp<nums[left-1]:
                nums[left] = nums[left-1]
                left -= 1
            nums[left] = temp
        