class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        beg = head
        end = head.next
        while end and end.next:
            temp = end.next
            end.next = end.next.next
            temp.next = beg.next
            beg.next = temp
            beg = beg.next
            end = end.next
        
        return head
            
        