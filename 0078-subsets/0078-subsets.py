class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.length = len(nums)
        self.helper([],nums,0)
        return self.ans
    
    def helper(self,arr,nums,ind):
        if ind < self.length:
            for i in range(ind,self.length):
                self.helper(arr+[nums[i]],nums,i+1)
        self.ans.append(arr)