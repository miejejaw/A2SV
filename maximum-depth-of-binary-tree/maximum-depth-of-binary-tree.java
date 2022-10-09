class Solution {
    int max=0;
    public int maxDepth(TreeNode root) {
        helper(root,1);
        return max;
    }
    public void helper(TreeNode root,int i){
        if(root==null) return;
        max=Math.max(max,i);
        helper(root.left,i+1);
        helper(root.right,i+1);
    }
}