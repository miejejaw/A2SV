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
            temp = slow.next
            newNode.next = rev
            rev = newNode
            slow = temp
            
        while rev:   
            if rev.val != head.val:
                return False
            rev = rev.next
            head = head.next
                                
        return True
            
            
        
        