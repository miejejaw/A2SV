class Solution {
    List<Integer> result = new LinkedList<>();
    public List<Integer> preorderTraversal(TreeNode root) {
        helper(root);
        return result;        
    }
    public void helper(TreeNode root){
        if(root==null) return;
        result.add(root.val);
        helper(root.left);
        helper(root.right);
    }
}