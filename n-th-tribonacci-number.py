class Solution:
    def __init__(self):
        self.d = {}
    def tribonacci(self, n: int) -> int:

        if n == 0: return 0
        elif n < 3: return 1
        elif n in self.d: return self.d[n]

        self.d[n] = self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3)
        return self.d[n]