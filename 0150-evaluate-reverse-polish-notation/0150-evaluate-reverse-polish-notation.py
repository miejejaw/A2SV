class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st= []
        for token in tokens:
            if token.isdigit():
                st.append(int(token))
            elif len(token)>1:
                st.append(-int(token[1:]))
            else:
                num2,num1 = st.pop(),st.pop()
                if token == "+":
                    st.append(num1+num2)
                elif token == "-":
                    st.append(num1-num2)
                elif token == "*":
                    st.append(num1*num2)
                else:
                    st.append(int(num1/num2))
                
        return st[0]