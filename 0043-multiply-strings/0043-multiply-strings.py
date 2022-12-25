class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        result = [0]*(len(num1)+len(num2))
        for i,n1 in enumerate(num1):
            temp = 0
            index = i
            for n2 in num2:
                temp += int(n1)*int(n2) + result[index]
                result[index] = temp%10 
                temp //= 10
                index += 1
            result[index] += temp
        ans = ''
        for x in result:
            ans = str(x) + ans
        ans = int(ans)
        return str(ans)
        