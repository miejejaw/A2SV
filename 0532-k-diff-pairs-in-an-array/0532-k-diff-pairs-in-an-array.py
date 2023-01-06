class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        dic = {}
        ans = set()
        for i,num in enumerate(nums):
            dic[-num] = i
        for i,num in enumerate(nums):
            temp = k-num
            if temp in dic and dic[temp]!=i:
                temp = (min(-num,temp) , max(-num,temp))
                if temp not in ans:
                    ans.add(temp)
        return len(ans)