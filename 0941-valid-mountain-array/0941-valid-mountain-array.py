class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        size = len(arr)
        if size<3 or arr[0]>=arr[1] or arr[-1]>=arr[-2]: 
            return False
        up = True
        for i in range(1,size):
            if up and arr[i]<arr[i-1]:
                up = False
            elif not up and arr[i]>=arr[i-1] or arr[i]==arr[i-1]:
                return False
                    
        return True
            
                