class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        result = nums[-2]+nums[-3]
        left = len(nums)-3
        right = len(nums)-1
        while left >= 0:
            if result > nums[right]:
                return result + nums[right]

            if left-1<0: 
                break
            result += nums[left-1]-nums[left+1]
            left -= 1
            right -= 1
        return 0
        