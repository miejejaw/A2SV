class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        n,ans = len(board),401
        visited = set({1})
        queue = deque([(1,0)])
 
        while queue:
            curr,steps = queue.popleft()
            if curr == n*n: ans = min(ans,steps)
            steps += 1
            for num in range(1,7):
                num += curr
                if num <= n*n:
                    x,y = self.getXY(num,n)
                    if board[x][y] != -1:
                        num = board[x][y]
                    if num not in visited:
                        queue.append((num,steps))
                        visited.add(num)

        return ans if ans != 401 else -1

    def getXY(self, num, n):
        row = ceil(num/n)
        col = num%n
        if row%2 == 1:
            col = n-1 if col == 0 else col-1
        elif col != 0:
            col = n - col
        return n-row,col