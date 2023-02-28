class MyCircularDeque:

    def __init__(self, k: int):
        self.size = k
        self.arr = []

    def insertFront(self, value: int) -> bool:
        if len(self.arr) < self.size:
            self.arr.insert(0,value)
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if len(self.arr) < self.size:
            self.arr.append(value)
            return True
        return False

    def deleteFront(self) -> bool:
        if self.arr:
            self.arr.pop(0)
            return True
        return False

    def deleteLast(self) -> bool:
        if self.arr:
            self.arr.pop()
            return True
        return False

    def getFront(self) -> int:
        if self.arr:
            return self.arr[0]
        return -1

    def getRear(self) -> int:
        if self.arr:
            return self.arr[-1]
        return -1

    def isEmpty(self) -> bool:
        if self.arr:
            return False
        return True

    def isFull(self) -> bool:
        if len(self.arr) == self.size:
            return True
        return False
