class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        length = len(intervals)
        ans = [-1]*length
        for ind in range(length):
            intervals[ind].append(ind)
        
        intervals.sort()
        for interval in intervals:
            left = 0
            right = length - 1
            while left < right:
                mid = left + (right-left)//2
                if interval[1] <= intervals[mid][0]:
                    right = mid
                else:
                    left = mid + 1
            if left < length and interval[1]<=intervals[left][0]:
                ans[interval[2]] = intervals[left][2]
        
        return ans