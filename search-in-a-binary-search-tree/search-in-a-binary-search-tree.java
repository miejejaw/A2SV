class Solution {
    TreeNode result = null;
    public TreeNode searchBST(TreeNode root, int val) {
        if(root!=null && result==null){
            if(root.val==val) result=root;
            searchBST(root.left,val);
            searchBST(root.right,val);
        }
       return result; 
    }
}