class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        return self.powerFour(n,1)
    
    def powerFour(self, n, pr):
        if pr == n:
            return True
        elif pr>n:
            return False
        return self.powerFour(n,pr*4)