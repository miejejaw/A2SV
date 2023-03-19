class Solution:
    def simplifyPath(self, path: str) -> str:
        
        st = ["/"]
        length,ind = len(path),0
        
        while ind < length:
            if path[ind] == "/":
                while ind < length and path[ind] == "/":
                    ind += 1
                if st and st[-1] != "/":
                    st.append("/")
            else:
                temp = ""
                while ind < length and path[ind] != "/":
                    temp += path[ind]
                    ind += 1
                if temp == "..":
                    if len(st)>1:
                        st.pop()
                        st.pop()
                elif temp != ".":
                    st.append(temp)
        if len(st) > 1 and st[-1] == "/":
            st.pop()

        return "".join(st)