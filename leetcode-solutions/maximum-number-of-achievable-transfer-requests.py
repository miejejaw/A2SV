class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:

        self.ans = 0
        self.length = len(requests)
        self.helper(requests,[0]*n,0,0,n)
        return self.ans

    def helper(self, arr, res, ind, count, n):
        if ind < self.length:
            for i in range(ind,self.length):
                res[arr[i][0]] -= 1
                res[arr[i][1]] += 1
                self.helper(arr,res,i+1,count+1,n)
                res[arr[i][0]] += 1
                res[arr[i][1]] -= 1

        if res.count(0) == n:
            self.ans = max(self.ans,count)