class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
                
        if not fast or not fast.next:
            return None
        
        slow = head 
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow