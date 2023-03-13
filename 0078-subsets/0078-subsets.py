class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.length = len(nums)
        self.helper([],nums,0)
        return self.ans
    
    def helper(self,arr,nums,ind):
        if ind < self.length:
            self.helper(arr+[nums[ind]],nums,ind+1)
            self.helper(arr,nums,ind+1)
            return 
        self.ans.append(arr)