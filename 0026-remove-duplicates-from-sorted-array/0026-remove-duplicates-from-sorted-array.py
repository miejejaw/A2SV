class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        beg,size = 0,len(nums)
        for end in range(1,size):
            if nums[end]!=nums[beg]:
                beg += 1
                nums[beg] = nums[end] 
        return beg+1