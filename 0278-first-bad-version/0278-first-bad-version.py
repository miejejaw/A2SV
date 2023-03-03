class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n-1
        
        while left <= right:
            
            mid = left + (right-left)//2
            if not isBadVersion(mid):
                left = mid+1
            else:
                right = mid-1
                
        return left
                