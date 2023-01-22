import functools
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str,nums))
        def compare(x,y):
            if (y+x >= x+y):
                return 1
            return -1
        
        nums = sorted(nums, key = functools.cmp_to_key(compare))
        res = "".join(nums)
        return res if res[0]!="0" else "0"
    
        