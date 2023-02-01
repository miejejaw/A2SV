class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        st = [head.val]
        fast = head
        slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            st.append(slow.val)
            
        if not fast.next:
            st.pop()
            
        while slow.next:
            slow = slow.next
            if slow.val == st[-1]:
                st.pop()
            else:
                break
                
        return st==[]
            
            
        
        