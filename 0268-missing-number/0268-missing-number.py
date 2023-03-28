class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        length = len(nums)
        ans = length
        for ind in range(length):
            while ind != nums[ind]: 
                
                if nums[ind] < length:
                    temp = nums[nums[ind]]
                    nums[nums[ind]] = nums[ind]
                    nums[ind] = temp
                else:
                    ans = ind
                    break
        return ans
        
                    
            
