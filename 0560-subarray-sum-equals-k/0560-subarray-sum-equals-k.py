class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        seen = defaultdict(int)
        seen[0] = 1
        total,count = 0,0
        
        for num in nums:
            total += num
            count += seen[total-k]   
            seen[total] += 1
            
        return count