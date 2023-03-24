class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.visited = set()
        self.length = len(nums)
        self.helper(nums,[],0)
        return self.ans
    
    def helper(self,nums,res,ind):
        
        if len(res) > 1 and tuple(res) not in self.visited:
            self.ans.append(res)
            self.visited.add(tuple(res))
        
        if ind < self.length:
            for i in range(ind,self.length):
                if not res or res[-1] <= nums[i]:
                    self.helper(nums,res+[nums[i]],i+1)
            
        
            