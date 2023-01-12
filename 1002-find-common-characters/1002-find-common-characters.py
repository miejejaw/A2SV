class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        dic = defaultdict(int)
        size = len(words)
        for ch in words[0]:
            dic[ch] += 1
            
        for ind in range(1,size):
            tempdic = defaultdict(int)
            for ch in words[ind]:
                tempdic[ch] += 1
            newdic = defaultdict(int)
            for ch in tempdic:
                if dic[ch]:
                    newdic[ch] = min(tempdic[ch],dic[ch])
            dic = newdic
        ans = []
        for ch,freq in dic.items():
            for _ in range(freq):
                ans.append(ch)
            
        return ans