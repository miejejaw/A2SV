class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        total = sum(weights)
        left = min(weights)
        right = total
        ans = total
        
        while left <= right:
            mid = left + (right-left)//2
            
            res = self.helper(weights,mid,days)
            if res:
                ans = min(ans,mid)
                right = mid - 1
            else:
                left = mid + 1
        return ans
        
    def helper(self,arr,mid,days):
        total = 0
        for num in arr:
            if mid < num:
                return False
            total += num
            if total > mid:
                days -= 1
                total = num
            
        if total > 0:
            days -= 1
        
        return True if days >= 0 else False
    