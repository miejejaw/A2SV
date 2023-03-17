class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            slow = head
            fast = head
            pev = None
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            list1 = self.sortList(slow)
            prev.next = None
            list2 = self.sortList(head)
            dummy = ListNode()
            
            self.helper(dummy,list1,list2)
            return dummy.next        
        return head
    
    def helper(self,curr,list1,list2):
        
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next    
            
        curr.next = None
        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2