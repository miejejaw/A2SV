class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        max_gap = 0
        nums.sort()
        arr_len = len(nums)
        for i in range(1,arr_len):
            max_gap = max(max_gap,nums[i]-nums[i-1])
        return max_gap