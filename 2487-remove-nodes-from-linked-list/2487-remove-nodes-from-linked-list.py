class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        st = []
        curr = head
        while curr:
            while st and curr.val > st[-1]:
                st.pop()
            st.append(curr.val)
            curr = curr.next
        
        size,ind = len(st),0
        dummy = ListNode(0,head)
        curr = dummy
       
        while curr.next and ind<size:
            if curr.next.val < st[ind]:
                curr.next = curr.next.next
            else:
                if curr.next.val == st[ind]:
                    ind += 1
                curr = curr.next
        
        return dummy.next
            