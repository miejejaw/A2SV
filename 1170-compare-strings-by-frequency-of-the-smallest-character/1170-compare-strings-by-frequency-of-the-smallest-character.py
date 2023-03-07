class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        words_length = len(words)
        queries_length = len(queries)
        for ind in range(words_length):
            words[ind] = self.findMinCount(words[ind])
        words.sort() 
        for ind in range(queries_length):
            freq = self.findMinCount(queries[ind])
            queries[ind] = words_length - self.findCount(freq,words)
        
        return queries
        
    def findMinCount(self,word):
        letter = "z"
        count = 0
        for ch in word:
            if ch < letter:
                letter = ch
                count = 0
            if letter == ch:    
                count += 1
        return count
    
    def findCount(self,num,words):
        left = 0
        right = len(words)
        while left < right:
            mid = left + (right-left)//2
            if words[mid] > num:
                right = mid
            else:
                left = mid + 1
        
        return left