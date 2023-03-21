class Solution:
    def balancedString(self, s: str) -> int:
        length = len(s)
        hold = {}
        for ch,freq in Counter(s).items():
            if freq > length/4:
                hold[ch] = freq - length//4
        
        if len(hold) == 0:
            return 0
        
        seen = defaultdict(int)
        visited = set()
        ans = length
        _len = len(hold)
        beg = 0
        for end in range(length):
            if s[end] not in hold:
                continue
            ch = s[end]
            seen[ch] += 1
            if seen[ch] >= hold[ch]:
                visited.add(ch)
                
            while len(visited) == _len:
                ans = min(ans,end-beg+1)
                if s[beg] in hold:
                    seen[s[beg]] -= 1
                    if seen[s[beg]] < hold[s[beg]]:
                        visited.remove(s[beg])
                beg += 1
        return ans
            
                