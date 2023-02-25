class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        postfix = [1]*size
        res = [0]*size
        for ind in range(size-2,-1,-1):
            postfix[ind] *= postfix[ind+1]*nums[ind+1]
            
        num = 1
        for ind in range(size):
            res[ind] = postfix[ind]*num
            num *= nums[ind]
            
        return res 