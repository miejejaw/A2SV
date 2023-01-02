class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        size = len(nums)
        for i,num in enumerate(nums):
            if i>0 and num == nums[i-1]:
                continue
            num = -num
            left = i+1
            right = size-1
            while right>left:
                
                temp = nums[right]+nums[left]
                if temp<num:
                    left += 1
                elif temp>num:
                    right -= 1
                else:
                    result.append([-num,nums[left],nums[right]])
                    while right>left and nums[right] == nums[right-1]:
                        right -= 1
                    while right>left and nums[left] == nums[left+1]:
                        print(left)
                        left += 1
                    right -= 1
                    left += 1
                    
        return result
            