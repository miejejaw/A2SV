from heapq import heapify,heappop,heappush
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        dummy = ListNode()
        curr = dummy
        length = len(lists)
        nums = []
        
        for ind in range(length):
            while lists[ind]:
                heappush(nums,lists[ind].val)
                lists[ind] = lists[ind].next
                    
        while nums:
            curr.next = ListNode(heappop(nums))
            curr = curr.next
        
        return dummy.next