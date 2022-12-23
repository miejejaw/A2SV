class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        result = -1
        index = 0 
        prev_min_distance = 10**5
        for pointX,pointY in points:
            if x==pointX or y==pointY:
                temp = abs(x-pointX) + abs(y-pointY)
                if temp < prev_min_distance:
                    prev_min_distance = temp
                    result = index
            index += 1
        return result