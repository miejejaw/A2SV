class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [0]*2
        
        for ind in range(length):
            j = nums[ind]-1
            while j != ind and nums[ind] != -1:
                if nums[ind] == nums[j]:
                    ans[0] = nums[ind]
                    ans[1] = ind + 1
                    nums[ind] = -1
                temp = nums[j]
                nums[j] = nums[ind]
                nums[ind] = temp
                j = nums[ind] - 1
                if nums[ind] == -1:
                    ans[1] = ind+1           
        
        return ans