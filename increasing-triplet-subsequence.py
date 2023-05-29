class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        length = len(nums)
        _min,_max = [0]*length,[0]*length
        _min[0] = nums[0]
        for ind in range(1,length):
            _min[ind] = min(_min[ind-1],nums[ind])

        _max[-1] = nums[-1]
        for ind in range(length-2,-1,-1):
            _max[ind] = max(_max[ind+1],nums[ind])

        
        for ind in range(1,length-1):
            if _min[ind]<nums[ind]<_max[ind]:
                return True
        
        return False