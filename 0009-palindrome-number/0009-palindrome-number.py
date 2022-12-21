class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        temp = ''
        for i in str(x):
            temp = i + temp
        return int(temp) == x
        
# 02
        