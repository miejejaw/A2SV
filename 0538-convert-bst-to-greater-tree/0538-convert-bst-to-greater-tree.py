class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.helper(root,0)
        return root
    
    def helper(self,curr,num):
        if curr:
            right = self.helper(curr.right,num) 
            curr.val += right + num
            left = self.helper(curr.left, curr.val)
            return curr.val-num + left
            
        return 0