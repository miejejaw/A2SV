class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.length = len(arr)
        self.ans = 0
        self.helper(arr,[0]*26,0,0)
        return self.ans
    
    def helper(self, arr, f, ind,s):
        self.ans = max(self.ans,s)
        
        if ind < self.length:
            for i in range(ind,self.length):
                temp = self.checker(f,arr[i])
                if temp[0]:
                    self.helper(arr,temp[1],i+1,s+len(arr[i]))
                
    def checker(self,arr,s):
        temp = arr[:]
        for ch in s:
            ind = ord(ch)-97
            if temp[ind] > 0:
                return [False,arr]
            temp[ind] += 1
            
        return [True,temp]
        