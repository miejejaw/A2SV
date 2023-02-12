class Solution:
    def reverseVowels(self, s: str) -> str:
        beg,end = 0,len(s)-1
        vowels = set({'a','A','e','E','i','I','o','O','u','U'})
        s = list(s)
        while beg<end:
            if s[beg] not in vowels:
                beg += 1
            elif s[end] not in vowels:
                end -= 1
            else:
                s[end],s[beg] = s[beg],s[end]
                beg += 1
                end -= 1
                
        return "".join(s)