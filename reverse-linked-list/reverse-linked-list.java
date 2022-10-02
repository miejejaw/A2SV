
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode h = new ListNode(0);
        helper(h,head);
        return h.next;
    }
    public ListNode helper(ListNode head, ListNode list){
        if(list==null) return null;
        ListNode temp= helper(head,list.next);
        
        if(temp==null) temp = head; 
        list.next = null;
        temp.next = list;
        return temp.next;
    }
}