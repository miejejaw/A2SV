class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        self.ans = False
        self.length = len(num)
        self.helper(num,0,'-1','-1')
        return self.ans
    
    def helper(self,num,ind,first_num,second_num):
        if ind < self.length and not self.ans:
            temp = ''
            total = int(first_num) + int(second_num)
            for i in range(ind, self.length):
                temp += num[i]
                if total == int(temp) or first_num == '-1':
                    self.helper(num,i+1,second_num,temp)
                elif total < int(temp):
                    return
                if int(temp) == 0 and i+1<self.length and num[i+1] != "0":
                    return
                
            return
        if first_num != '-1' and first_num + second_num != num:
            self.ans = True
            