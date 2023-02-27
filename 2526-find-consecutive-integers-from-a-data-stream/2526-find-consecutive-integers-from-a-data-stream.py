class DataStream:

    def __init__(self, value: int, k: int):
        self.val = value
        self.length = 0
        self.k = k
        self.size = 0
        self.que = deque()

    def consec(self, num: int) -> bool:
        self.que.append(num)
        self.length += 1
        if num == self.val:
            self.size += 1
        
        if self.length > self.k:
            if self.que.popleft() == self.val:
                self.size -= 1
            self.length -= 1        
        if self.size == self.k and num == self.val:
            return True
        return False