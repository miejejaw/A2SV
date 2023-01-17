class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        res = set()
        for num in nums:
            res.add(num)
            temp = 0
            while num:
                temp = temp*10 + num%10
                num //= 10
            res.add(temp)    
        return len(res)