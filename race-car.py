from collections import deque
class Solution:
    def racecar(self, target: int) -> int:
        
        seen = set((0,1))
        queue = deque([(0,1,0)])
        
        while queue:
            pos,speed,d = queue.popleft()
            if pos+speed == target:
                return d+1
            
            if (pos+speed,speed*2) not in seen:
                queue.append((pos+speed,speed*2,d+1))
                seen.add((pos+speed,speed*2))
                
            speed = -1 if speed>0 else 1
            if (pos,speed) not in seen:
                queue.append((pos,speed,d+1))
                seen.add((pos,speed))