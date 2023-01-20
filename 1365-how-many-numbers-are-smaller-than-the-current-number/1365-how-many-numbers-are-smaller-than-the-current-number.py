class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        size = len(nums)
        temp = [[num,ind] for ind,num in enumerate(nums)]
        temp.sort()
        prev = temp[0][0]
        temp[0][0] = 0
        nums[temp[0][1]] = 0
        for ind in range(1,size):
            if prev==temp[ind][0]:
                temp[ind][0] = temp[ind-1][0]
            else:
                prev = temp[ind][0]
                temp[ind][0] = ind
            nums[temp[ind][1]] = temp[ind][0]
            
        return nums
                
                