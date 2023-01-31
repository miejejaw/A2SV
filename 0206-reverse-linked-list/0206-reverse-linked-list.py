class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = None
        while head:
            temp = head
            head = head.next
            temp.next = node
            node = temp
            
        return node
        