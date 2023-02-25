class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        size = len(nums)
        seen = defaultdict(int)
        seen[0] = 1
        total,count = 0,0
        
        for ind in range(size):
            total += nums[ind]
            if total-k in seen:
                count += seen[total-k]
                
            seen[total] += 1
            
        return count