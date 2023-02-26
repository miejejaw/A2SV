class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        seen = defaultdict(int)
        for passengers,beg,end in trips:
            seen[end] -= passengers
            seen[beg] += passengers
            
        prev = 0
        for num in sorted(seen):
            prev += seen[num]
            if prev > capacity:
                return False
        
        return True