class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        self.kthLargest(nums,0,len(nums)-1,len(nums)-k)
        return nums[-k]
    
    def kthLargest(self, nums, low, high, k):
        
        pivot = high
        high -= 1
        left = low

        while low < high:
            if nums[low] < nums[pivot]:
                low += 1
            elif nums[high] >= nums[pivot]:
                high -= 1
            else:
                nums[low],nums[high] = nums[high],nums[low]
                low += 1
                high -= 1
        if nums[low] >= nums[pivot]:
            nums[low],nums[pivot] = nums[pivot],nums[low]
        else:
            nums[low+1],nums[pivot] = nums[pivot],nums[low+1]
            low += 1
        if low > k:
            self.kthLargest(nums,left,low-1,k)
        elif low < k:
            self.kthLargest(nums,low+1,pivot,k)