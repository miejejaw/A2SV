class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        temp,num = x,0      
        while temp>0:
            num = num*10 + temp%10 
            temp //= 10
        return num == x
        
# 02
        