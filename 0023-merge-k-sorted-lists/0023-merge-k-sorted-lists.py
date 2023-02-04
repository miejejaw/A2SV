class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        size = len(lists)
        j = 0
        while j<size:
            if not lists[j]:
                del lists[j]
                size -= 1
            else: 
                j += 1
        
        while lists:
            j = 0
            for i in range(1,size):
                if lists[j].val>lists[i].val:
                    j = i
            curr.next = lists[j]
            curr = curr.next
            lists[j] = lists[j].next
            if not lists[j]:
                del lists[j]
                size -= 1
        curr.next = None
        return dummy.next