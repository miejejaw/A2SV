class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        curr = head
        res = [0]*k
        ind = 0
        while curr:
            curr = curr.next
            res[ind%k] += 1
            ind += 1
            
        curr = head    
        for i in range(k):
            n = res[i]-1
            res[i] = curr
            if curr:
                for _ in range(n):
                    curr = curr.next

                temp = curr
                curr = curr.next
                temp.next = None
        return res
            