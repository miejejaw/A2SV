class Solution:
    def partitionString(self, s: str) -> int:
        res = 0
        seen = set()
        for ch in s:
            if ch in seen:
                res += 1
                seen.clear()
            seen.add(ch)
        if seen:
            res += 1
        return res