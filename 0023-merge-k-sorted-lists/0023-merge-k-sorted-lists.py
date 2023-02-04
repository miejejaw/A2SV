class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        size = len(lists)
       
        while True:
            j = float("inf")
            k = -1
            for i in range(size):
                if lists[i] and j>lists[i].val:
                    j = lists[i].val
                    k = i
            if k==-1:
                break
            curr.next = lists[k]
            curr = curr.next
            lists[k] = lists[k].next
            
        curr.next = None
        return dummy.next
#10min