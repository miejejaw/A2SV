class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        st = []
        size = len(nums)-1
        num = float("-inf")
        for ind in range(size,-1,-1):
            while st and nums[ind]>st[-1]:
                num = st.pop()
                
            if st and num>nums[ind]:
                return True
            st.append(nums[ind])
                
        return False