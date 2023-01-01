class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        spaces_len = len(spaces)
        j = 0
        for i,ch in enumerate(s):
            if spaces_len>j and spaces[j]==i:
                result.append(" ")
                j += 1
            result.append(ch)
            
        return "".join(result)