from heapq import heapify,heappop,heappush
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        dummy = ListNode()
        curr = dummy
        length = len(lists)
        nums,hasNum = [],True
        while hasNum:
            for ind in range(length):
                if lists[ind]:
                    hasNum = False
                    heappush(nums,lists[ind].val)
                    lists[ind] = lists[ind].next
            if not hasNum: 
                hasNum = True
            else:
                break
            curr.next = ListNode(heappop(nums))
            curr = curr.next
            
        while nums:
            curr.next = ListNode(heappop(nums))
            curr = curr.next
        
        return dummy.next