class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        length = len(nums)
        ans = 1
        for ind in range(length):
            if nums[ind] > length:
                nums[ind] = 0
            j = nums[ind]-1
            while j >= 0 and j != ind:
                if nums[j] == nums[ind]:
                    nums[ind] = -1
                
                temp = nums[j]
                nums[j] = nums[ind]
                nums[ind] = temp
                j = nums[ind] - 1
                
        for ind in range(length):
            if nums[ind] <= 0:
                return ind+1
            
        return length+1