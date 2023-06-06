class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        
        length = len(nums)
        count,beg = 0,-1
        num = nums[0]
        for end in range(length):
            if nums[end]%k != 0:
                beg = end
                if end+1 < length: num = nums[end+1]
                continue

            for ind in range(end,beg,-1):
                if gcd(nums[end],nums[ind]) == k:
                    count += ind-beg
                    break
            num = min(num,nums[end])       
        return count