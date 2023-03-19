class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        
        _len = len(votes[0])
        res = [[]]*26
        for ch in votes[0]:
            ind = ord(ch)-65
            res[ind] = [0]*_len + [-ord(ch)]
        
        for vote in votes:
            for ind in range(_len):
                num = ord(vote[ind])-65
                res[num][ind] += 1
        
        res.sort(reverse = True)
        ans = []
        for v in res:
            if v:
                ch = chr(-v[-1])
                ans.append(ch)
            
        return "".join(ans)
        
                