class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        st = []
        length = len(nums)
        res = [-1]*len(nums)
        for index in range(length*2):
            ind = index%length
            while st and nums[ind] > nums[st[-1]]:
                res[st.pop()] = nums[ind] 
            st.append(ind)
        
        return res