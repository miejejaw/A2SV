class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        size = len(nums)
        for i,num in enumerate(nums):
            num = -num
            left = i+1
            right = size-1
            while right>left:
                temp = nums[right]+nums[left]
                if temp==num:
                    result.add((-num,nums[left],nums[right]))
                    right -= 1
                    left += 1
                elif temp>num:
                    right -= 1
                else:
                    left += 1
        result = map(list,result)
        return result
            