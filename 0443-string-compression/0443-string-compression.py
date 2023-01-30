class Solution:
    def compress(self, chars: List[str]) -> int:
        count,beg = 1,0
        size = len(chars)
        
        for end in range(1,size):
            if chars[end] == chars[end-1]:
                count += 1   
            else:
                chars[beg] = chars[end-1]
                beg += 1
                if count>1:
                    for ch in str(count):
                        chars[beg] = ch
                        beg += 1
                count = 1
        chars[beg] = chars[-1]
        beg += 1
        if count>1: 
            for ch in str(count):
                chars[beg] = ch
                beg += 1
                
        return beg
                                    
                    
        