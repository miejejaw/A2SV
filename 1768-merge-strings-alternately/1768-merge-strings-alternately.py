class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        size = min(len(word1),len(word2))
        temp  = word1[size:] + word2[size:]
        result = ''
        for index in range(size):
            result += word1[index]
            result += word2[index]
        return result + temp