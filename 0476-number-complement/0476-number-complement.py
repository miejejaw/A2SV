class Solution:
    def findComplement(self, num: int) -> int:
        
        res = 0
        ind = 0
        while num > 0:
            if num & 1 == 0:
                res += 2**ind
                
            ind += 1
            num >>= 1
        
        return res