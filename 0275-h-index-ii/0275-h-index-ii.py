class Solution:
    def hIndex(self, citations: List[int]) -> int:
        length = len(citations)
        left = 0
        right = length - 1
        
        while left <= right:
            mid = left + (right-left)//2
            if length-mid <= citations[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return length-left