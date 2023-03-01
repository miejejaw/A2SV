class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        ans = self.helper(nums,0,len(nums)-1,True)
        if ans[0] >= ans[1]:
            return True
        return False
    def helper(self, nums,l,r, pt):
        if l == r:
            if pt:
                return [nums[l],0]
            return [0,nums[l]]
        
        if pt:
            left = self.helper(nums,l+1,r,not pt )
            left[0] += nums[l]
            
            right = self.helper(nums,l,r-1,not pt )
            right[0] += nums[r]
            
            return left if left[0]>right[0] else right
        else:
            left = self.helper(nums,l+1,r,not pt )
            left[1] += nums[l]
            
            right = self.helper(nums,l,r-1,not pt )
            right[1] += nums[r]
            
            return left if left[1]>right[1] else right
            