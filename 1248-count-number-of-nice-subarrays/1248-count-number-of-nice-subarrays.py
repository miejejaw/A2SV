class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        beg,size = 0,len(nums)
        for ind in range(size):
            nums[ind] %= 2
        nums = accumulate(nums)
        nums = Counter(nums)
        nums[0] += 1
        res = 0
        size = len(nums)
        for ind in range(k,size):
            res += nums[ind]*nums[ind-k]
        return res
                
        