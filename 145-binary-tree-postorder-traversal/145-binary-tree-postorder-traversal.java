class Solution {
    List<Integer> result = new LinkedList<>();
    public List<Integer> postorderTraversal(TreeNode root) {
         if(root!=null){
            postorderTraversal(root.left);
            postorderTraversal(root.right);
            result.add(root.val);
        }
        return result;  
    }
}