from collections import defaultdict
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        count = 0 
        for num in nums:
            if num in dic:
                count += dic[num]
            dic[num] += 1
        return count