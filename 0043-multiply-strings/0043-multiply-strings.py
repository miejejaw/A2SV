class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        result = [0]*(len(num1)+len(num2))
        num1_len = len(num1)-1
        num2_len = len(num2)-1

        for num1_idx in range(num1_len,-1,-1):         
            index = num1_idx + num2_len + 1
            temp = 0
            for num2_idx in range(num2_len,-1,-1):           
                temp += int(num1[num1_idx])*int(num2[num2_idx]) + result[index]
                result[index] = temp%10 
                temp //= 10
                index -= 1
            result[index] += temp

        ans = ''
        for x in result:
            ans += str(x)
        ans = int(ans)
        return str(ans)
        