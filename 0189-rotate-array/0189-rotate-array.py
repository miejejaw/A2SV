class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        
        i,j = len(nums)-k-1,0       
        while i>j:
            nums[j],nums[i] = nums[i],nums[j]
            i-=1
            j+=1
            
        j,i = len(nums)-k,len(nums)-1
        while i>j:
            nums[j],nums[i] = nums[i],nums[j]
            i-=1
            j+=1
            
        i,j = len(nums)-1,0
        while i>j:
            nums[j],nums[i] = nums[i],nums[j]
            i-=1
            j+=1