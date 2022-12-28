class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        dic = {}
        hold = collections.defaultdict(int)
        i = 1
        count = 0
        for _ in range(22):
            dic[i] = 0
            i *= 2
            
        for num in deliciousness:
            for x,val in dic.items():
                temp = x-num
                if temp in hold:
                    count += hold[temp]
            
            hold[num] += 1
        return count % (10**9 + 7)