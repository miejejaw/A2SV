class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        hold = Counter(p)
        seen = defaultdict(int)
        beg,length = 0,len(s)
        res = []
        
        for end in range(length):
            if s[end] not in hold:
                while beg < end:
                    seen[s[beg]] -= 1
                    if seen == hold:
                        res.append(beg)
                    beg += 1
                beg += 1
                continue
                
            seen[s[end]] += 1
            if seen[s[end]] > hold[s[end]]:
                while seen[s[end]] > hold[s[end]]:
                    seen[s[beg]] -= 1
                    beg += 1
                
            if seen == hold:
                res.append(beg)
        
        return res
            
                    