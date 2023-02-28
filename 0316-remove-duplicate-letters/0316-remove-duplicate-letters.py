class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        seen = set()
        length = len(s)
        st,dic = [],{}
        for ind in range(length):
            dic[s[ind]] = ind
            
        for ind,ch in enumerate(s):
            if ch not in seen:
                while st and st[-1] > ch:
                    if dic[st[-1]] < ind:
                        break
                    seen.remove(st.pop())
                seen.add(ch)
                st.append(ch)       
            
        return "".join(st)