class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        self.kthLargest(nums,0,len(nums)-1,len(nums)-k)
        return nums[-k]
    
    def kthLargest(self, nums, low, high, k):
        
        pivot = nums[high]
        left,right = low,high
        high -= 1

        while low <= high:
            if nums[low] < pivot:
                low += 1
            elif nums[high] >= pivot:
                high -= 1
            else:
                nums[low],nums[high] = nums[high],nums[low]
                low += 1
                
        nums[low],nums[right] = nums[right],nums[low]

        if low > k:
            self.kthLargest(nums,left,low-1,k)
        elif low < k:
            self.kthLargest(nums,low+1,right,k)