class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = defaultdict(int)
        res = []
        for num in nums1:
            dic[num] += 1
        
        for num in nums2:
            if dic[num]>0:
                res.append(num)
                dic[num] -= 1
        
        return res