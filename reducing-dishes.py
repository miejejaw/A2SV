class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:

        length = len(satisfaction)
        satisfaction.sort()
        ans = 0
        for i in range(length):
            total = 0
            for j in range(i,length):
                total += satisfaction[j]*(j-i+1)
            ans = max(ans,total)

        return ans