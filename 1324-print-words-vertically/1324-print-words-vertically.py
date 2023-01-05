class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        size = len(max(s, key=len))
        ans = []
        for i in range(size):
            temp = []
            for word in s:
                if i<len(word):
                    temp.append(word[i])
                else:
                    temp.append(" ")
            temp = "".join(temp).rstrip()
            ans.append(temp)
        return ans