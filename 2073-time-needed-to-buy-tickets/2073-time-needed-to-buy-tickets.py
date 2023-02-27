class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        size = len(tickets)
        ans = 0
        while tickets[k]:
            for ind in range(size):
                if tickets[ind] != 0:
                    tickets[ind] -= 1
                    ans += 1
                    if tickets[k] == 0:
                        return ans

        return 0