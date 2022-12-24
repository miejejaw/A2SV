class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hold = {}
        size = len(arr)
        index = 0
        for num in arr:
            hold[num] = index
            index += 1
        for index,num in enumerate(arr):
            if num*2 in hold and hold[num*2] != index:
                return True
        return False