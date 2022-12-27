from collections import defaultdict
class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count = 0
        dic = defaultdict(lambda : 0)
        
        for i, word in enumerate(words):
            word = "".join(sorted(set(word)))
            count += dic[word]
            dic[word] += 1
         
        return count
        