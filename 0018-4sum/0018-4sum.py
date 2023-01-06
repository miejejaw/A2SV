class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()
        nums_len =len(nums)
        for i,num in enumerate(nums):
            if i>0 and num==nums[i-1]:
                continue
            for j in range(i+1,nums_len):
                if j-1 != i and nums[j]==nums[j-1]:
                    continue
                temp = target - (num+nums[j])
                left,right = j+1,nums_len-1
                while right>left:
                    num_sum = nums[left]+nums[right]
                    if temp>num_sum:
                        left += 1
                    elif temp<num_sum:
                        right -= 1
                    else:
                        ans.append([num,nums[j],nums[left],nums[right]])
                        while right>left and nums[left]==nums[left+1]:
                            left += 1
                        while right>left and nums[right]==nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
        return ans
                    