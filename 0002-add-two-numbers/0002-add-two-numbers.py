# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        curr = dummy
        temp = 0
        while l1 and l2:
            temp += l1.val+l2.val
            curr.next = ListNode(temp%10)
            curr = curr.next
            temp //= 10
            l1 = l1.next
            l2 = l2.next
            
        while l1:
            temp += l1.val
            curr.next = ListNode(temp%10)
            curr = curr.next
            temp //= 10
            l1 = l1.next 
            
        while l2:
            temp += l2.val
            curr.next = ListNode(temp%10)
            curr = curr.next
            temp //= 10
            l2 = l2.next
        if temp>0:
            curr.next = ListNode(temp)
        return dummy.next