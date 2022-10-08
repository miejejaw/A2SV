class Solution {
    List<Integer> result = new LinkedList<>();
    public List<Integer> inorderTraversal(TreeNode root) {
        helper(root);
        return result;  
    }
    public void helper(TreeNode root){
        if(root==null) return;
        
        helper(root.left);
        result.add(root.val);
        helper(root.right);
    }
}