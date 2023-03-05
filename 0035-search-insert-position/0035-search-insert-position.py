class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        beg = 0
        end = len(nums)-1
        while beg <= end:
            mid = beg + (end-beg)//2
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                beg = mid + 1
            else:
                return mid
        return beg