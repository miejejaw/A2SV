class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if 0<=c<=1:
            return True
        arr = set()
        for num in range(c):
            temp = num**2
            arr.add(temp)
            if c-temp in arr:
                return True
            if temp>c:
                break
            
        return False



