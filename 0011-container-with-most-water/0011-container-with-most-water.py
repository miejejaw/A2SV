class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        beg,end = 0,len(height)-1
        while end>beg:
            area = max(area,(end-beg)*min(height[beg],height[end]))
            
            if height[end]>=height[beg]:
                beg += 1
            elif height[beg]>height[end]:
                end -= 1
            else:
                end -= 1
                beg += 1 
            
        return area