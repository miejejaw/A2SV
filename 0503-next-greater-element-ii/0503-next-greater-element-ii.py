class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        st = []
        length = len(nums)
        res = [-1]*len(nums)
        for ind in range(length*2):
            while st and nums[ind%length] > nums[st[-1]]:
                res[st.pop()] = nums[ind%length] 
            st.append(ind%length)
        
        return res