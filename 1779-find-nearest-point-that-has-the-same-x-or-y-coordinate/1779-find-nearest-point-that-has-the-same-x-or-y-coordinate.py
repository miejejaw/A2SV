class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        result = -1
        prev_min_distance = 10**5
        for index,point in enumerate(points):
            if x==point[0] or y==point[1]:
                temp = abs(x-point[0]) + abs(y-point[1])
                if temp < prev_min_distance:
                    prev_min_distance = temp
                    result = index
        return result