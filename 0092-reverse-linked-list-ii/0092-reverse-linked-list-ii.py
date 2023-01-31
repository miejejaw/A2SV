
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if right==left: return head
        dummy = ListNode()
        dummy.next = head
        
        lists = dummy
        for _ in range(1,left):
            lists = lists.next
                    
        ptr = lists
        temp = lists.next
        node = None
        for _ in range(right-left+1):
            newNode = temp
            temp = temp.next
            newNode.next = node
            node = newNode
            
        ptr.next = node  
        while ptr.next:
            ptr = ptr.next
        ptr.next = temp
        
        return dummy.next
            