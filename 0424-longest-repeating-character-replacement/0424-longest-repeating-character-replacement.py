class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        size = len(s)
        seen = set(s)
        for ch in seen:
            beg,count = 0,k
            for end in range(size):
                if s[end] != ch and count>0:
                    count -= 1
                elif s[end] != ch: 
                    while beg<=end and count <= 0:
                        if s[beg] != ch:
                            count += 1
                        beg += 1
                    count -= 1
                res = max(res,end-beg+1)
                
        return res
                    
                