class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        size = len(arr)
        if size==1:
            return []
        while True:
            end = 1
            while end <size and arr[end]>arr[end-1]:
                end += 1
            if end == size:
                break
            elif end>1:
                self.helper(arr,end-1)
                res.append(end)
            res.append(arr[0])
            self.helper(arr, arr[0]-1)
        return res        
                
    def helper(self, arr, end):
        beg = 0
        while end>beg:
            arr[end],arr[beg] = arr[beg],arr[end]
            beg += 1
            end -= 1
    
                
                