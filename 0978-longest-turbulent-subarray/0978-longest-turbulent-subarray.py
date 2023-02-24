class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        size = len(arr)
        res = 1
        beg = 0
        for end in range(size-1):
            if (end%2==1 and arr[end]<=arr[end+1]) or (end%2==0 and arr[end]>=arr[end+1]):
                res = max(res,end-beg+1)
                beg = end+1
            if end+2 == size:
                res = max(res,end-beg+2)    
            res = max(res,end-beg+1)
            
        beg = 0   
        for end in range(size-1):
            if (end%2==0 and arr[end]<=arr[end+1]) or (end%2==1 and arr[end]>=arr[end+1]):
                res = max(res,end-beg+1)
                beg = end+1
            if end+2 == size:
                res = max(res,end-beg+2)
            res = max(res,end-beg+1)
            
        return res