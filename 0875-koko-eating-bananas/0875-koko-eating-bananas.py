class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        total = sum(piles)
        left = 1
        right = total

        while left < right:
            mid = left + (right-left)//2
            
            if self.helper(piles,mid,h):
                right = mid
            else:
                left = mid + 1
                
        return left
        
    def helper(self,arr,mid,hours):
        hour = 0
        for num in arr:
            hour += ceil(num/mid)   
        
        return hours >= hour