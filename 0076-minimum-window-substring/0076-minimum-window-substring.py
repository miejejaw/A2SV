class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hold = Counter(t)
        m = len(hold)
        seen = defaultdict(int)
        ss = set()
        beg = n = 0
        length = len(s)
        gap = length+1
        a = b =0
        for end in range(length):
            seen[s[end]] += 1
            if s[end] in hold and seen[s[end]] == hold[s[end]]:
                ss.add(s[end])
                n += 1
            while m == n:
                if gap > end-beg+1:
                    gap = end-beg+1
                    a = beg
                    b = end
                seen[s[beg]] -= 1
                if s[beg] in ss and seen[s[beg]] < hold[s[beg]]:
                    ss.remove(s[beg])
                    n -= 1
                beg += 1
        ans = ""
        if gap <= length: 
            ans = s[a:b+1]
        return ans