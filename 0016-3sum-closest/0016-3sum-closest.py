class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = float('inf')
        size = len(nums)
        for i in range(size):
            if i>0 and nums[i] == nums[i-1]:
                continue
                
            left = i+1
            right = size-1
            while right>left:
                
                temp = nums[right]+nums[left]+nums[i]
                if abs(target-result) > abs(target-temp):
                    result = temp
                if temp<target:
                    left += 1
                elif temp>target:
                    right -= 1
                else:
                    return temp
                                        
        return result        