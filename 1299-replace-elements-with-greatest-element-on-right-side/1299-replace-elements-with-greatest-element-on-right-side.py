class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        num = -1
        size = len(arr)
        for i in range(size):
            temp = arr[~i]
            arr[~i] = num
            num = max(num,temp)
        return arr
        