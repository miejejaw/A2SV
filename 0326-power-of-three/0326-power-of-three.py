class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        return self.powerThree(n,1)
    
    def powerThree(self, n, pr):
        if pr == n:
            return True
        elif pr>n:
            return False
        return self.powerThree(n,pr*3)