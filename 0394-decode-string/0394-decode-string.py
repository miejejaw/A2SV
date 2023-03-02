class Solution:
    def decodeString(self, s: str) -> str:
        res = []
        beg = 0
        length = len(s)
        while beg < length:
            temp  = self.helper(s,beg,length)
            beg = temp[1]
            res += temp[0]
        return "".join(res)
    
    def helper(self, s, beg, length):
        if beg>=length:
            return ["",beg]
        if s[beg].isdigit():
            num = 0
            while beg<length and s[beg].isdigit():
                num = num*10 + int(s[beg])
                beg += 1
            beg += 1
            word = []
            while beg<length and s[beg]!="]":
                if s[beg].isdigit():
                    res = self.helper(s,beg,length)
                    word += res[0]
                    beg = res[1]
                else:
                    word.append(s[beg])
                    beg += 1
            temp = "".join(word) 
            word = [temp]*num           
            return [word,beg+1]
            
        else:
            word = []
            while beg<length and not s[beg].isdigit():
                word.append(s[beg])
                beg += 1
                
            if beg == length:
                return [word,beg]
            res = self.helper(s,beg,length)
            return [word + res[0],res[1]]
            