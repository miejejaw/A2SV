class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        max_points = 0
        for i in range(len(points)):
            dic = collections.defaultdict(int)
            x1,y1 = points[i]
            for j in range(i+1,len(points)):
                x2,y2 = points[j]
                temp = 'v' if x2==x1 else (y2-y1)/(x2-x1)
                
                dic[temp] += 1
                max_points = max(max_points,dic[temp])
                
        return max_points+1