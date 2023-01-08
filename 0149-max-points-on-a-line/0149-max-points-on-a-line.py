class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        
        max_points = 0
        for i in range(len(points)):
            dic = collections.defaultdict(set)
            x1,y1 = points[i]
            for j in range(len(points)):
                if i==j: continue
                x2,y2 = points[j]
                temp = 'v' if x2==x1 else (y2-y1)/(x2-x1)
                
                dic[temp].add((x2,y2))
                max_points = max(max_points,len(dic[temp]))
                
        return max_points+1