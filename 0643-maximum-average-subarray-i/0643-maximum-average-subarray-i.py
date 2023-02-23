class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = sum(nums[:k])
        size = len(nums)
        res = total/k
        for ind in range(k,size):
            total += nums[ind] - nums[ind-k]
            res = max(res,total/k)
            
        return res