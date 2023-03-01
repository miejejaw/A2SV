class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        st = []
        length = len(nums)
        num = float("-inf")
        
        for ind in range(length-1,-1,-1):
            if num>nums[ind]:
                return True
            while st and nums[ind]>st[-1]:
                num = st.pop()         
            st.append(nums[ind])
                
        return False