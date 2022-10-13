class Solution {
    Stack<Integer> temp = new Stack<>();
    boolean ans= true;
    public boolean isValidBST(TreeNode root) {
        if(root!=null && ans){
            isValidBST(root.left);
            if(!temp.isEmpty() && temp.peek()>=root.val) ans=false;
            temp.push(root.val);
            isValidBST(root.right);   
        }        
        return ans;
    }
}