class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ans = 0
        for num,freq in sorted(Counter(nums).items(),reverse=True):
            if k-freq <= 0:
                return num
            k -= freq
