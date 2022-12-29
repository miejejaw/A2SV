class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        dic = defaultdict(int)
        count = 0           
        for num in deliciousness:
            pow2 = 1
            for _ in range(22):
                num2 = pow2-num
                if num2 in dic:
                    count += dic[num2]
                pow2 *= 2
            
            dic[num] += 1
        return count % (10**9 + 7)