class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        res = set(nums)
        for num in nums:
            res.add(int(str(num)[::-1]))    
        return len(res)