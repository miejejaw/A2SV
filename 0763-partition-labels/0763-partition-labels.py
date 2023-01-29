class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = defaultdict(list)
        size = len(s)
        for ind,ch in enumerate(s):
            if s[ind] in dic:
                dic[ch][1] = ind
            else:
                dic[ch].append(ind)
                dic[ch].append(ind)
        
        arr = list(dic.values())
        res = []
        num = arr[0][1]
        pr = -1
        for nums in arr:
            if num>=nums[0]:
                num = max(num,nums[1])
            else:
                res.append(num-pr)
                pr = num
                num = nums[1]
        res.append(num-pr)
        
        return res