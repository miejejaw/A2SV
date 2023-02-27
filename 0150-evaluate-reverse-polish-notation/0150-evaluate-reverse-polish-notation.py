class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st= []
        num = float("-inf")
        for token in tokens:
            if token.isdigit() or len(token)>1:
                st.append(token)
            else:
                num2,num1 = st.pop(),st.pop()
                res = eval(num1+token+num2)
                st.append(str(int(res)))
                
        return int(st[0])