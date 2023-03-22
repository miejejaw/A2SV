class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        
        st = []
        length = len(heights)
        res = [0]*length
        
        for ind in range(length):
            while st and heights[st[-1][0]] <= heights[ind]:
                temp = st.pop()
                res[temp[0]] = temp[1]
                if st:
                    st[-1][1] += 1
                    
            st.append([ind,1])
        st.pop()    
        while st:
            temp = st.pop()
            res[temp[0]] = temp[1]
 
        return res