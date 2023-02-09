class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        res,st = [],[]
        ind = 0
        while head:
            while st and head.val>st[-1][0]:
                val,index = st.pop()
                res[index] = head.val
            
            st.append((head.val,ind)) 
            res.append(0)
            head = head.next
            ind += 1
        
        return res
        