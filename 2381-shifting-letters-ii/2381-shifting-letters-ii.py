class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        size = len(s)
        res = [0]*(size+1)
        for shift in shifts:
            if shift[2] == 0:
                res[shift[0]] -= 1
                res[shift[1]+1] += 1
            else:
                res[shift[0]] += 1
                res[shift[1]+1] -= 1
                
        res.pop()       
        for ind,val in enumerate(accumulate(res)):
            temp = ord(s[ind]) + val%26
            if temp>122:
                res[ind] = chr(temp-26)
            elif temp<97:
                res[ind] = chr(temp+26)
            else:
                res[ind] = chr(temp)
               
        return "".join(res)
            
            