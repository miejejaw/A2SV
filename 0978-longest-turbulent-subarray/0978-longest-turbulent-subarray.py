class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        size = len(arr)
        res = 1
        beg = 0
        for end in range(1,size):
            if (end%2==1 and arr[end-1]<=arr[end]) or (end%2==0 and arr[end-1]>=arr[end]):
                beg = end   
            res = max(res,end-beg+1)
            
        beg = 0   
        for end in range(1,size):
            if (end%2==0 and arr[end-1]<=arr[end]) or (end%2==1 and arr[end-1]>=arr[end]):
                beg = end
            res = max(res,end-beg+1)
            
        return res