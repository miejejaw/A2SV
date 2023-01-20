class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        size = len(nums)
        temp = nums.copy()
        temp.sort()
        prev = temp[0]
        temp[0] = 0
        dic = {prev:0}
        for ind in range(1,size):
            if prev==temp[ind]:
                temp[ind] = temp[ind-1]
            else:
                prev = temp[ind]
                temp[ind] = ind
            dic[prev] = temp[ind]
        for ind in range(size):
            nums[ind] = dic[nums[ind]]
        return nums
                
                