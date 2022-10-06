class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> result = new LinkedList<>();
        Stack<TreeNode> st = new Stack<>();
        while(root!=null){
            if(root.left!=null) {
                st.push(root); 
                root=root.left;
            }
            else{
              result.add(root.val);               
              if(root.right!=null) root=root.right;
              else if(!st.isEmpty()){ 
                  root=st.pop();
                  root.left=null;
              }
              else root=null; 
            }            
        }
        return result;       
    }
}