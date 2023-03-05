class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        total = sum(weights)
        left = max(weights)
        right = total
        ans = total
        
        while left < right:
            mid = left + (right-left)//2
            
            if self.helper(weights,mid,days):
                right = mid
            else:
                left = mid + 1
        return left
        
    def helper(self,arr,mid,days):
        total = 0
        day = 1
        for num in arr:
            total += num
            if total > mid:
                day += 1
                total = num
        
        return days >= day
    