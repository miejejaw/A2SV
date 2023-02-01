class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        slow = slow.next 
        rev = None
        while slow: 
            newNode = slow
            slow = slow.next
            newNode.next = rev
            rev = newNode
            
        while rev:   
            if rev.val != head.val:
                return False
            rev = rev.next
            head = head.next
                                
        return True
            
            
        
        