class Solution:
    def splitString(self, s: str) -> bool:
        self.ans = False
        self.length = len(s)
        self.helper([],s,0)
        return self.ans
    
    def helper(self,arr,s,ind):
            
        if not self.ans and ind < self.length:
            temp = ''
            for i in range(ind,self.length):
                temp += s[i]
                if arr and int(arr[-1]) < int(temp):
                    return
                if arr and int(arr[-1]) - int(temp) != 1:
                    continue
                else:
                    self.helper(arr+[temp],s,i+1)
            return
        
        if len(arr)>1:
            self.ans = True