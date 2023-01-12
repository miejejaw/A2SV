class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        maindic = [0]*26
        size = len(words)
        for ch in words[0]:
            maindic[ord(ch)-97] += 1
            
        for ind in range(1,size):
            tempdic = [0]*26
            for ch in words[ind]:
                tempdic[ord(ch)-97] += 1
                
            for i in range(26):           
                maindic[i] = min(tempdic[i],maindic[i])

        ans = []
        for ind,freq in enumerate(maindic): 
            ans += [chr(ind+97)]*freq
            
        return ans