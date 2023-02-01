class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next
        
        dummey = ListNode(0,head)
        curr = dummey   
        for _ in range(size-n):
            curr = curr.next
            
        curr.next = curr.next.next
        return dummey.next