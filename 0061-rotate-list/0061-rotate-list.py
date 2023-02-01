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
        k = size-1 - k%size
        
        nodes = nodes[k::-1] + nodes[:k:-1]
            
        head = temp
        for val in reversed(nodes):
            head.val = val
            head = head.next
        return temp