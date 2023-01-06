class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count = 0
        for cost in costs:
            coins -= cost
            if coins<0:
                break
            count += 1
        return count