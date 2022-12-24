class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        size = len(arr)
        index = 0
        while size > index:
            if arr[index] == 0:
                right = size-1
                while right > index:
                    arr[right] = arr[right-1]
                    right -= 1
                index += 1
            index += 1
        