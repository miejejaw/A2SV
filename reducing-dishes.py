class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:

        length = len(satisfaction)
        satisfaction.sort()
        ans = total = 0
        
        for i in range(length-1,-1,-1):
            total += satisfaction[i]
            if total <= 0: break
            ans +=  total
            
        return ans