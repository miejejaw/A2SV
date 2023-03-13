class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.total = sum(cookies)
        self.ans = self.total
        self.length = len(cookies)
        self.k = k
        self.helper([0]*k,cookies,0,0)
        return self.ans
    
    def helper(self, arr, cookies, i,c):
        if self.total > self.ans < arr[c]:
            return
        if i < self.length:
            for j in range(self.k):
                arr[j] += cookies[i]
                self.helper(arr,cookies,i+1,j)
                arr[j] -= cookies[i]  
            return 
        self.ans = min(self.ans,max(arr))