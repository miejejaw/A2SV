class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.ans = inf
        self.length = len(cookies)
        cookies.sort(reverse = True)
        self.helper([0]*k,cookies,0,0,k)
        return self.ans
    
    def helper(self, arr, cookies, ind,c,k):
        if ind < self.length:
            for j in range(k):
                if arr[j] + cookies[ind] < self.ans:
                    arr[j] += cookies[ind]
                    self.helper(arr,cookies,ind+1,j,k)
                    arr[j] -= cookies[ind]  
            return 
        self.ans = min(self.ans,max(arr))