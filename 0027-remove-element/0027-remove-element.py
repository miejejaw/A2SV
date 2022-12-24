class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        size = len(nums)
        left = 0
        for index in range(size):
            if nums[index] != val:
                nums[left] = nums[index]
                left += 1
        return left