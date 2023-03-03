class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left = 1
        right = x//2
        mid = 0
        while left <= right:
            mid = left + (right-left)//2
            if mid*mid < x:
                left = mid + 1
            elif mid*mid > x:
                right = mid - 1
            else:
                return mid
        if right*right <= x:
            return right
        elif left*left <= x:
            return left
            