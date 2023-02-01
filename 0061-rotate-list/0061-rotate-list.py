# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k==0:
            return head
        temp = head
        nodes = []
        while head:
            nodes.append(head.val)
            head = head.next
        size = len(nodes)
        k = k%size
        # print(list(reversed(nodes[:size-k])), list(reversed(nodes[size-k:]))       
        nodes = list(reversed(nodes[:size-k])) + list(reversed(nodes[size-k:]))
        
        # print(nodes[size-k::-1] , nodes[:k:-1])
        
        nodes = nodes[::-1]
        
        head = temp
        for ind in range(size):
            head.val = nodes[ind]
            head = head.next
        return temp