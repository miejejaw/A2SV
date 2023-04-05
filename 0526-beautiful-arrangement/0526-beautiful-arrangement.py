class Solution:
    def countArrangement(self, n: int) -> int:
        self.count = 0
        self.helper(n+1,0,1)
        return self.count
        
    def helper(self,n,num,ind):
        if ind < n:
            for i in range(1,n):
                if num & (1<<(i-1)) == 0 and (i%ind==0 or ind%i==0):
                    self.helper(n,num|(1<<(i-1)),ind+1)
            return 
        
        if bin(num).count("1") == n-1:
            self.count += 1
    
    
    
    
    
    
    
    
    
    
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14
# 15