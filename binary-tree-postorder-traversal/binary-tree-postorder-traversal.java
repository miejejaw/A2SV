class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> result = new LinkedList<>();
        Stack<TreeNode> st = new Stack<>();
        st.push(null);
        while(root!=null){
            if(root.left!=null) {
                TreeNode temp =root.left;
                root.left=null;
                st.push(root); 
                root=temp;
            }
            else{                          
              if(root.right!=null) {
                  TreeNode temp =root.right;
                  root.right=null;
                  st.push(root);
                  root=temp;
              }
              else{ 
                  result.add(root.val);
                  root=st.pop(); 
              }
            }            
        }
        return result;
    }
}