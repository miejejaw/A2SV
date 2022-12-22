class Solution:
    def freqAlphabets(self, s: str) -> str:
        st,ans = [],''
        for ch in s:
            if '#' == ch:
                temp1 = st.pop()
                temp2 = st.pop()+temp1
                st.append(temp2)
            else: 
                st.append(ch)
        while len(st)>0:
            ans = chr(96+int(st.pop())) + ans
        return ans