class Solution:
    def findComplement(self, num: int) -> int:
        
        res = 0
        ind = 0
        while num:
            if not num & 1:
                res += 2**ind
                
            ind += 1
            num >>= 1
        
        return res