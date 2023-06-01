class Solution:    
    def gcd(self,a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        
        freq = list(Counter(deck).values())
        gcd_value = freq[0]
        for num in freq:
            gcd_value = self.gcd(gcd_value,num)
            
        return gcd_value > 1