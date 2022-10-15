class Solution {
    boolean ans =false;
    public boolean hasPathSum(TreeNode root, int targetSum) {
        helper(root,targetSum);
        return ans;
    }
    public void helper(TreeNode root, int target){
        if(root==null || ans) return;
        target-=root.val;
        if(target==0 && root.left==null && root.right==null)
           ans=true;
        helper(root.left,target);
        helper(root.right,target);
    }
}