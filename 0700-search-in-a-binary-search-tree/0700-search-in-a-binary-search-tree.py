class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root:
            if root.val == val:
                return root
            
            left = self.searchBST(root.left,val)
            right = self.searchBST(root.right,val)
            
            if left or right:
                return left if left else right