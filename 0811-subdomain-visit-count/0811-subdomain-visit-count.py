class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic = defaultdict(int)
        for cpdomain in cpdomains:
            rep,domain = cpdomain.split()
            rep = int(rep)
            dic[domain] += rep
            while domain.find('.')!=-1:
                idx = domain.find('.')+1
                domain = domain[idx:]
                dic[domain] += rep
        ans = []
        for key,val in dic.items():
            temp = str(val) + " " + key
            ans.append(temp)
        return ans