class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        seen = set()
        size = len(nums)
        beg=end=ans=0
        k -= 1
        total = 0
        for end in range(size):
            if nums[end] in seen:
                while nums[end]!=nums[beg]:
                    seen.remove(nums[beg])
                    total -= nums[beg]
                    beg += 1
                seen.remove(nums[beg])
                total -= nums[beg]
                beg += 1
            seen.add(nums[end])
            total += nums[end]
            
            if end-beg == k:
                ans = max(ans,total)
                seen.remove(nums[beg])
                total -= nums[beg]
                beg += 1
                
        return ans