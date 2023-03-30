class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        length = len(nums)
        for ind in range(length):
            j = nums[ind]-1
            while j != ind:
                if nums[j] == nums[ind]:
                    return nums[ind]
                
                nums[ind] = nums[j]
                nums[j] = j+1
                j = nums[ind]-1
                
        return 0