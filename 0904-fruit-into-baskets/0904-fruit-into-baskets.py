class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        size = len(fruits)
        beg = res = 0
        seen = defaultdict(int)
        for end in range(size):
            seen[fruits[end]] += 1
            while len(seen) > 2:
                seen[fruits[beg]] -= 1
                if seen[fruits[beg]] == 0:
                    seen.pop(fruits[beg])
                beg += 1
            res = max(res,end-beg+1)
        return res