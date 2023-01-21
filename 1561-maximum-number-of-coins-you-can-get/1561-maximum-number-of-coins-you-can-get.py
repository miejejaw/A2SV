class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        count = 0
        size = len(piles)
        for ind in range(size//3,size,2):
            count += piles[ind]
        return count