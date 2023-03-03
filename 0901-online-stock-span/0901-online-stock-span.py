class StockSpanner:

    def __init__(self):
        self.st = []

    def next(self, price: int) -> int:
        count = 1
        while self.st and price >= self.st[-1][0]:
            count += self.st.pop()[1]
            
        self.st.append((price,count))
        return count