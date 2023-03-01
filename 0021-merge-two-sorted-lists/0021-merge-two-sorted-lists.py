class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        self.mergeLists(list1,list2,dummy)
        return dummy.next
    
    def mergeLists(self, list1, list2, curr):
        if not list1 and not list2:
            curr.next = None
            return 
        elif not list1:
            curr.next = list2
            return
        elif not list2:
            curr.next = list1
            return 
        if list1.val >= list2.val:
            curr.next = list2
            list2 = list2.next
        else:
            curr.next = list1
            list1 = list1.next
        self.mergeLists(list1,list2,curr.next)