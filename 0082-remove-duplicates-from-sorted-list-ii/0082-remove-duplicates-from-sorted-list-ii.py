class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        left = dummy
        curr = head
        
        while curr:
            flag = False
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
                flag = True
                
            if flag:
                left.next = curr.next
            else:
                left = left.next
            curr = curr.next
            
        return dummy.next
    