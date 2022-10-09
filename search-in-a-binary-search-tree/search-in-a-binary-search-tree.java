class Solution {
    TreeNode node = null;
    public TreeNode searchBST(TreeNode root, int val) {
        if(root!=null){
            if(root.val==val) node=root;
            searchBST(root.left,val);
            searchBST(root.right,val);
        }
       return node; 
    }
}