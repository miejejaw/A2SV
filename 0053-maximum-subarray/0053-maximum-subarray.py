class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        size = len(nums)
        st = [0]
        res = float("-inf")
        for ind,num in enumerate(accumulate(nums)):
            while st and num<=st[-1]:
                st.pop()
            st.append(num)
            if st[0] != st[-1]:
                res = max(res,st[-1]-st[0])
            else:
                 res = max(res,nums[ind])
            
        return res