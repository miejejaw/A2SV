class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        ans = 0
        for i in range(len(nums)):
            nums[i] += pow(2,31)
            
        for i in range(32):
            count = 0
            temp = 1 << i
            for num in nums:
                if temp & num:
                    count += 1
                    
            if count%3:
                ans += pow(2,i)
            
        return ans-pow(2,31)