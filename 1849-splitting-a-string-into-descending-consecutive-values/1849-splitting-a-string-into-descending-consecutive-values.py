class Solution:
    def splitString(self, s: str) -> bool:
        self.ans = False
        self.length = len(s)
        self.helper([],s,0)
        return self.ans
    
    def helper(self,arr,s,ind):
        if ind == self.length and len(arr)>1:
            self.ans = True
            
        if not self.ans:
            temp = ''
            for i in range(ind,self.length):
                temp += s[i]
                # if arr and int(arr[-1]) - int(temp) > 1 :
                #     return
                if arr and int(arr[-1]) - int(temp) != 1:
                    continue
                else:
                    self.helper(arr+[temp],s,i+1)