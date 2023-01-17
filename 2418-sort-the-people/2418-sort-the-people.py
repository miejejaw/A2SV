class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        size = len(names)
        for i in range(size):
            ind = i
            for j in range(i+1,size):
                if heights[j]>heights[ind]:
                    ind = j
                    
            heights[i],heights[ind] = heights[ind],heights[i]
            names[i],names[ind] = names[ind],names[i]
        return names