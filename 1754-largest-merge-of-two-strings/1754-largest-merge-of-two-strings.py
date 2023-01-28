class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        i,j = 0,0
        i_len = len(word1)
        j_len = len(word2)
        res = []
        while i<i_len and j<j_len:
            if word1[i:]>word2[j:]:
                res.append(word1[i])
                i += 1
            else:
                res.append(word2[j])
                j += 1
        res.append(word1[i:])
        res.append(word2[j:])
        return "".join(res)
                