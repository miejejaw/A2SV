class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dic_lose = collections.defaultdict(int)
        for winner,loser in matches:
            if winner not in dic_lose:
                dic_lose[winner] = 0
            dic_lose[loser] += 1
            
        lost_one = []
        win_all = []
        for i,freq in dic_lose.items():
            if freq == 0:
                win_all.append(i)
            elif freq == 1:
                lost_one.append(i)
        return [sorted(win_all), sorted(lost_one)]