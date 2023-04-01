class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        return self.find_GCD(min(nums),max(nums))
        
    def find_GCD(self,a,b):
        if b == 0:
            return a
        return self.find_GCD(b,a%b)


