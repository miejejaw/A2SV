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
                
        res = list(accumulate(res))
        ans = [0]*size
        for ind in range(size):
            temp = ord(s[ind]) + res[ind]%26
            if temp>122:
                ans[ind] = chr(temp-26)
            elif temp<97:
                ans[ind] = chr(temp+26)
            else:
                ans[ind] = chr(temp)
                
        return "".join(ans)
            
            