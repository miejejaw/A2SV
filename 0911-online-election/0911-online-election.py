class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.board = [0]*len(times)
        dic = defaultdict(int)
        max_ = persons[0]
        for ind,person in enumerate(persons):
            dic[person] += 1
            if dic[person] >= dic[max_]:
                max_ = person
           
            self.board[ind] = max_
            
    def q(self, t: int) -> int:
        left = 0
        right = len(self.times)-1
        
        while left <= right:
            mid = left + (right-left)//2
            if t < self.times[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        return self.board[right]

        