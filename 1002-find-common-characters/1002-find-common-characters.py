class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        dic = [0]*26
        size = len(words)
        for ch in words[0]:
            dic[ord(ch)-97] += 1
            
        for ind in range(1,size):
            tempdic = [0]*26
            for ch in words[ind]:
                tempdic[ord(ch)-97] += 1
            newdic = [0]*26
            for ind,freq in enumerate(tempdic):           
                newdic[ind] = min(tempdic[ind],dic[ind])
            dic = newdic
        ans = []
        for ind,freq in enumerate(dic): 
            ans += [chr(ind+97)]*freq
            
        return ans