class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        seen[0] = 1
        count = 0
        for ind,num in enumerate(accumulate(nums)):
            if num%k in seen:
                count += seen[num%k]
            seen[num%k] += 1
            
        return count