class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        st = []
        while head:
            while st and head.val>st[-1]:
                st.pop()
            st.append(head.val)
            head = head.next
            
        dummy = ListNode() 
        curr = dummy
        for val in st:
            curr.next = ListNode(val)
            curr = curr.next
            
        return dummy.next