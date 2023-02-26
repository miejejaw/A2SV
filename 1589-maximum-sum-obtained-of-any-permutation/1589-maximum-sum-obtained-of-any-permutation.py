class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        size = len(nums)
        res = [0]*size
        for beg,end in requests:
            res[end] += 1
            if beg>0:
                res[beg-1] -= 1
        
        for ind in range(size-2,-1,-1):
            res[ind] += res[ind+1]
        res.sort()
        nums.sort()
        ans = 0
        for ind in range(size):
            ans += nums[ind]*res[ind]
            
        return ans%(10**9+7)