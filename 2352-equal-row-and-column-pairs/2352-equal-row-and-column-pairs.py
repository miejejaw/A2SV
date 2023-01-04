class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        dic = collections.defaultdict(int)
        count = 0
        for row in zip(*grid):
            dic[row] += 1
        for row in grid:
            count += dic[tuple(row)]
        return count