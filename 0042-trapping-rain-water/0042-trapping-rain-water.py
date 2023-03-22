class Solution:
    def trap(self, height: List[int]) -> int:
        st = []
        res,length = 0,len(height)
        
        for ind in range(length):
            while st and height[st[-1]] <= height[ind]:
                temp = st.pop()
                if st :
                    h = min(height[st[-1]],height[ind]) - height[temp]
                    res += h * (ind-st[-1]-1)
                    
            st.append(ind)
            
        return res