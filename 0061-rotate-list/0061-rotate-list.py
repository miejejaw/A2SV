class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k==0:
            return head
        
        temp = prev = head
        size = 0
        while temp:
            size += 1
            prev = temp
            temp = temp.next
        
        if 0 == k%size:
            return head
        
        temp = head     
        for i in range(size- k%size-1):
            temp = temp.next
        
        newHead = temp.next
        temp.next = None    
        prev.next = head 
        
        return newHead

        