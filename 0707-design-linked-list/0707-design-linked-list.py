class Node:
    def __init__(self,val,nextNode):
        self.val = val
        self.next = nextNode
        
class MyLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int: 
        curr = self.head
        ind = 0
        while ind!=index and curr:
            curr = curr.next
            ind += 1
        if curr:
            return curr.val
        return -1

    def addAtHead(self, val: int) -> None:

        newNode = Node(val,None)
        if not self.head:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
            
    def addAtTail(self, val: int) -> None:
        
        newNode = Node(val,None)
        if not self.head:
            self.head = newNode
        else:
            curr = self.head
            while curr.next:
                curr = curr.next         
            curr.next =  newNode
        
    def addAtIndex(self, index: int, val: int) -> None:
        
        newNode = Node(val,None)
        if index == 0:
            newNode.next = self.head
            self.head = newNode
        else:
            curr = self.head
            ind = 0
            while ind+1<index and curr:
                curr = curr.next
                ind += 1
            if curr:
                temp = curr.next
                curr.next = newNode
                newNode.next = temp

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.head = self.head.next
        else:
            curr = self.head
            ind = 0
            while ind+1<index:
                curr = curr.next
                ind += 1
            if curr and curr.next:
                curr.next = curr.next.next
            elif curr:
                curr.next = None
