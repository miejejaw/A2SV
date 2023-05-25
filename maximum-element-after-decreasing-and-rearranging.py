class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        
        arr.sort()
        res = 1
        for num in arr:
            if num != res:
                res += 1
            
        return res-1 if res > len(arr) else res