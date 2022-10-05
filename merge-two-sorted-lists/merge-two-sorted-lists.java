/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode head = new ListNode(0);
        helper(head,list1,list2);
        return head.next;
    }
    public void helper(ListNode list, ListNode list1, ListNode list2){
        if(list1==null && list2==null) return;
        else if(list1==null) {list.next=list2; return;}
        else if(list2==null) {list.next=list1; return;}
        
        ListNode temp;
        list.next=null;
        if(list1.val<list2.val){
            temp=list1;
            list1=list1.next;
        }
        else{
            temp=list2;
            list2=list2.next;
        }
        list.next=temp;
        helper(list.next,list1,list2);
    }
}