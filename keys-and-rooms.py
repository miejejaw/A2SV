class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        length = len(rooms)
        visited = [1]*length
        self.bfs(rooms,[0],visited)
        return sum(visited) == 0
    
    def bfs(self, rooms, keys, visited):
        
        newKeys = []
        for key in keys:
            visited[key] = 0
            for room in rooms[key]:
                if visited[room]:
                    newKeys.append(room)
        if newKeys:
            self.bfs(rooms,newKeys,visited)