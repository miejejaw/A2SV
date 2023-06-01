class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        
        res = []
        for num,freq in Counter(deck).items():
            res.append(freq)
            
        if min(res) == 1: return False
        
        length = len(res)
        d = defaultdict(int)
        
        for num in res:
            p = 2
            while p*p <= num:
                while num%p == 0: 
                    d[p] += 1
                    while num%p == 0: num //= p
                p += 1
            if num > 1: d[num] += 1
                      
        for k,v in d.items():
            if v == length: return True
          
        return False