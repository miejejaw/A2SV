class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = {}
        for ind,ch in enumerate(s):
            if s[ind] in dic:
                dic[ch][1] = ind
            else:
                dic[ch] = [ind,ind]
        
        res = []
        partion = [-1,dic[s[0]][1]]
        for nums in dic.values():
            if nums[0]<=partion[1]:
                partion[1] = max(partion[1],nums[1])
            else:
                res.append(partion[1]-partion[0])
                partion[0] = partion[1]
                partion[1] = nums[1]
        res.append(partion[1]-partion[0])
        
        return res