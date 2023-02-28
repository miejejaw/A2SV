class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        size,res = len(arr),1
        beg1 = beg2= 0
        
        for end in range(1,size):
            if (end%2==1 and arr[end-1]<=arr[end]) or (end%2==0 and arr[end-1]>=arr[end]):
                beg1 = end   
            res = max(res,end-beg1+1)
      
            if (end%2==0 and arr[end-1]<=arr[end]) or (end%2==1 and arr[end-1]>=arr[end]):
                beg2 = end
            res = max(res,end-beg2+1)
            
        return res