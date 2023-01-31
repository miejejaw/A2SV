class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        ind,size = 0,len(players)
        
        for num in trainers:
            if ind<size and num>=players[ind]:
                ind += 1
                
        return ind