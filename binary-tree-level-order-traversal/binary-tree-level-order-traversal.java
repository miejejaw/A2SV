class Solution {
    List<List<Integer>> result = new LinkedList<>();
    public List<List<Integer>> levelOrder(TreeNode root) {
        helper(root,0);
        return result;
    }
    public void helper(TreeNode root, int i){
        if(root==null) return;
        if(i==result.size()) result.add(new LinkedList<Integer>());
        helper(root.left,i+1);
        helper(root.right,i+1);
        result.get(i).add(root.val);
    }
}