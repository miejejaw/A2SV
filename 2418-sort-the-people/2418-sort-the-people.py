class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        size = len(names)
        end = size
        for i in range(size):
            isswap = False
            for j in range(1,end):
                if heights[j]>heights[j-1]:
                    heights[j],heights[j-1] = heights[j-1],heights[j]
                    names[j],names[j-1] = names[j-1],names[j]
                    isswap = True
            if not isswap:
                break
        return names