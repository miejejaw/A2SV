class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        beg,end = head,head
        curr = None
        while end and end.next:
            temp = beg
            beg = beg.next
            end = end.next.next
            temp.next = curr
            curr = temp
        
        res = 0
        while curr:
            res = max(res,curr.val+beg.val)
            curr = curr.next
            beg = beg.next
        
        return res
        