class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0,head)
        curr = dummy.next
        
        while curr and curr.next:
            if curr.val > curr.next.val:
                temp = curr.next
                curr.next = curr.next.next
                ptr = dummy
                while ptr.next.val < temp.val:
                    ptr = ptr.next
                temp.next = ptr.next
                ptr.next = temp
            else:
                curr = curr.next
            
        
        return dummy.next
        