class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        
        self.count = defaultdict(int)
        self.helper(0,nums,0,len(nums))
        num = max(self.count, key = self.count.get)
        return self.count[num]
                
    def helper(self,num,nums,ind,n):
        if ind < n:
            for i in range(ind,n):
                self.helper(num|nums[i],nums,i+1,n)
        self.count[num] += 1