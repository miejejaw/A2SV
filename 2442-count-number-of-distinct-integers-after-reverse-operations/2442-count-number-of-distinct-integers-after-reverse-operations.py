class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        res = set(nums)
        for num in nums:
            temp = 0
            while num:
                temp = temp*10 + num%10
                num //= 10
            res.add(temp)    
        return len(res)