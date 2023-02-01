class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        bigger = ListNode()
        smaller = ListNode()
        big_ptr = bigger
        smaller_ptr = smaller
        
        while head:
            temp = head
            head = head.next
            temp.next = None
            if temp.val<x:
                smaller.next = temp
                smaller = smaller.next
            else:
                bigger.next = temp
                bigger = bigger.next
        smaller.next = big_ptr.next
        return smaller_ptr.next
            