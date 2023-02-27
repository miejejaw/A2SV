class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        st = []
        for p in s:
            if p == "(":
                st.append("(")
            elif st[-1] == "(":
                st.pop()
                if st and st[-1] != "(":
                    st[-1] += 1
                else:
                    st.append(1)
            else:
                temp = st.pop()*2
                st.pop()
                if st and st[-1] != "(":
                    st[-1] += temp
                else:
                    st.append(temp)
                
                
        return st[0]
    
