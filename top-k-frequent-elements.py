class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        arr = []
        for num,freq in Counter(nums).items():
            arr.append((num,freq))
            
        self.quickselect(arr,0,len(arr)-1,len(arr)-k)
        ans = [arr[~i][0] for i in range(k)]
        return ans
    
    def quickselect(self, nums, low, high, k):
        
        pivot = nums[high][1]
        left,right = low,high
        high -= 1

        while low <= high:
            if nums[low][1] < pivot:
                low += 1
            elif nums[high][1] >= pivot:
                high -= 1
            else:
                nums[low],nums[high] = nums[high],nums[low]
                low += 1
                
        nums[low],nums[right] = nums[right],nums[low]

        if low > k:
            self.quickselect(nums,left,low-1,k)
        elif low < k:
            self.quickselect(nums,low+1,right,k)