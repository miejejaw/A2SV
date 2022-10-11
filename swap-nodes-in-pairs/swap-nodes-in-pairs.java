class Solution {
    public ListNode swapPairs(ListNode head) {
        ListNode h = new ListNode(0);
        h.next=head;
        helper(h);
        return h.next;
    }
    public void helper(ListNode list){
        if(list.next==null || list.next.next==null) return;
        ListNode temp = list.next.next;
        list.next.next = list.next.next.next;
        temp.next=list.next;
        list.next= temp;
        helper(list.next.next);
    }
}