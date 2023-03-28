class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        length = len(nums)
        for ind in range(length):
            j = nums[ind]-1
            while nums[ind] != ind+1 and nums[j] != j+1:
                nums[ind],nums[j] = nums[j],nums[ind]
                j = nums[ind]-1
                
        ans = []       
        for ind in range(length):
            if nums[ind] != ind+1:
                ans.append(ind+1)
        
        return ans