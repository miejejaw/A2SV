class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:

        length = len(arr)
        for ind in range(length-1,0,-1):
            if arr[ind] < arr[ind-1]:
                j = length-1
                while arr[ind-1] <= arr[j] or arr[j]==arr[j-1]:
                    j -= 1
                arr[j],arr[ind-1] = arr[ind-1],arr[j]
                return arr
        return arr