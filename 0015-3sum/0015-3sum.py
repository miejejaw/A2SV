class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dic = {}
        result = set()
        # nums.sort()
        for i,num in enumerate(nums):
            dic[num] = i
        for i,num1 in enumerate(nums):
            for j in range(i+1,len(nums)):
                temp = -(num1+nums[j])
                if temp in dic and dic[temp]!=j and dic[temp]!=i:
                    temp = tuple(sorted((num1,nums[j],temp)))
                    result.add(temp)

        return map(list,result)
        
            