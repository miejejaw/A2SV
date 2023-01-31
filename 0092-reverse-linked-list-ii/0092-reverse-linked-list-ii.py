
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if right==left:
            return head
        dummy = ListNode()
        dummy.next = head
        
        lists = dummy
        for _ in range(1,left):
            lists = lists.next
                    
        ptr = lists
        temp = lists.next
        node = None
        while left<=right and temp:
            newNode = temp
            temp = temp.next
            newNode.next = node
            node = newNode
            left += 1
            
        ptr.next = node  
        while ptr.next:
            ptr = ptr.next
        ptr.next = temp
        
        return dummy.next
            