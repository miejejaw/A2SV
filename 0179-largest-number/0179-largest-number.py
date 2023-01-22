class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str,nums))
        def compare(x,y):
            if (y+x >= x+y):
                return 1
            return -1
        
        nums = sorted(nums, key = cmp_to_key(compare))
        return "".join(nums).lstrip("0") or "0"
    
        