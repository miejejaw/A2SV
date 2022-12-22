class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i, word in enumerate(words):
            temp = ''
            for l in word:
                temp += chr(97+order.index(l))
            words[i] = temp
        for i in range(len(words)-1):
            if words[i]>words[i+1]:
                return False
        return True