class Solution {
    long temp = Long.MIN_VALUE;
    boolean ans= true;
    public boolean isValidBST(TreeNode root) {
        if(root!=null && ans){
            isValidBST(root.left);
            if(temp>=root.val) ans=false;
            temp=root.val;
            isValidBST(root.right);   
        }        
        return ans;
    }
}