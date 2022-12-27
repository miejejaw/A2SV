import math
class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count = 0
        dic = {}
        for i, word in enumerate(words):
            word = "".join(sorted("".join(set(word))))
            dic[word] = dic.get(word ,0)+1
        for i,val in dic.items():
            for i in range(1,val):
                count += i
                
        return count
        