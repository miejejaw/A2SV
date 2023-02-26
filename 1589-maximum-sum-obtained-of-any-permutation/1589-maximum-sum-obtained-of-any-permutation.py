class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        ans,size = 0,len(nums)
        res = [0]*(size+1)
        for beg,end in requests:
            res[beg] += 1
            res[end+1] -= 1
            
        res.pop()
        res = sorted(accumulate(res))
        nums.sort()
        for ind in range(size):
            ans += nums[ind]*res[ind]
            
        return ans%(10**9+7)