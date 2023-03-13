class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ans = []
        self.helper([],n,k,1)
        return self.ans
    
    def helper(self, arr, n, k, ind):
        if len(arr) == k:
            self.ans.append(arr)
            return
        if ind > n:
            return
        
        self.helper(arr+[ind],n,k,ind+1)
        self.helper(arr,n,k,ind+1)