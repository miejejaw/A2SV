class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        res = []
        nums.sort()
        for ind,num in enumerate(nums):
            if num==target:
                res.append(ind)
        return res