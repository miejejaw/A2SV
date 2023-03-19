class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        st = []
        res = []
        for num in arr:
            temp = 1
            while st and st[-1][0] > num:
                temp += st.pop()[1]
            
            res.append(temp)
            st.append((num,temp))

        st = []
        ans = 0
        for ind in range(len(arr)-1,-1,-1):
            num = arr[ind]
            temp = 1
            while st and st[-1][0] >= num:
                temp += st.pop()[1]
            
            res[ind] *= temp
            ans += res[ind] * num
            st.append((num,temp))
        
        return ans%(10**9+7)
            
            