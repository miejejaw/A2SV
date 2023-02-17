class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        num1 = num2 = num3 = float("-inf")
        count = 0
        for num in nums:
            if num>num3 and num!=num2 and num!=num1:
                num3 = num
                if num3 > num2:
                    num2,num3 = num3,num2
                    if num2 > num1:
                        num1,num2 = num2,num1
                count += 1
        if count<3:
            return max(num1,num2,num3)
        return num3
            
                