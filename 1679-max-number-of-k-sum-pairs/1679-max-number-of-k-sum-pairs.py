class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        beg,end = 0,len(nums)-1
        res = 0
        while end>beg:
            total = nums[end]+nums[beg]
            if total>k:
                end -= 1
            elif total<k:
                beg += 1
            else:
                end -= 1
                beg += 1
                res += 1
        return res