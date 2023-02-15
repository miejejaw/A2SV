class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k==1:
            return 0
        nums.sort()
        ans = nums[-1]
        k -= 1
        for ind in range(k,len(nums)):
            ans = min(ans,nums[ind]-nums[ind-k])
        return ans