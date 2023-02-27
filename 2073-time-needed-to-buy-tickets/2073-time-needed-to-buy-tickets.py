class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        if tickets[k] == 0:
            return 0
        size = len(tickets)
        num = tickets[k]
        ans = 0
        for ind in range(size):
            if ind <= k:
                ans += min(num,tickets[ind])
            else:
                ans += min(num-1,tickets[ind])

        return ans